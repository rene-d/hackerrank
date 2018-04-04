#!/bin/bash
#set -x
#echo $* >> runtest-cmdline.txt

# program parameters
rootdir=$(dirname "$0")
verbose=
number=
contest_slug=master
testcase=

# program usage
usage()
{
    echo "Usage: runtest.sh [options]"
    echo "  -h,--help       : help"
    echo "  -t,--testcase   : testcase name"
    echo "  -n,--number     : testcase number"
    echo "error $1"
    exit $1
}


set_colors()
{
    if [ -t 1 -a -t 0 ]; then
        COLOR_RED="\033[91m"
        COLOR_GREEN="\033[92m"
        COLOR_YELLOW="\033[93m"
        COLOR_LIGHT_PURPLE="\033[94m"
        COLOR_PURPLE="\033[95m"
        COLOR_END="\033[0m"
    else
        COLOR_RED=
        COLOR_GREEN=
        COLOR_YELLOW=
        COLOR_LIGHT_PURPLE=
        COLOR_PURPLE=
        COLOR_END=
    fi
}

# compare command
compare()
{
    python3 "${rootdir}/compare.py" "$1" "$2"
}

close_std()
{
    if [ $CTEST_INTERACTIVE_DEBUG_MODE ]; then
        # close stdout and stderr
        exec 1<&-
        exec 2<&-

        # open stdout as a file for read and write.
        exec 1<>$testname.log

        # redirect stderr to stdout
        exec 2>&1
    fi
}


download_pdf()
{
    pdf="${rootdir}/statements/$testname.pdf"
    [ -s "$pdf" ] && return

    mkdir -p "${rootdir}/statements"

    url="https://www.hackerrank.com/rest/contests/${contest_slug}/challenges/$testname/download_pdf?language=English"
    curl -s -L -o "${pdf}" "${url}"
    if [ ! -s "${pdf}" ]; then
        rm -f "${pdf}"
        echo "Download problem: ${url}"
        exit 2
    fi
}


download_zip()
{
    [ -s "${testcases}" ] && return

    url="https://www.hackerrank.com/rest/contests/${contest_slug}/challenges/${testname}/download_testcases"
    curl -s -L -o "${testcases}" "${url}"
    if [ ! -s "${testcases}" ]; then
        rm -f "${testcases}"
        echo "Download problem: ${url}"
        exit 2
    fi
}

# read the options
if [ "$(uname)" = "Darwin" ]; then
    ARGS=`getopt hvn:t: $*`
else
    ARGS=`getopt -o hvn:t: --long help,verbose,contest:,number:,test: -n 'runtest.sh' -- "$@"`
fi
eval set -- "$ARGS"
[ $? != 0 ] && usage 2

# extract options and their arguments into variables.
for i ; do
    case "$i" in
        -h|--help) usage ;;
        -v|--verbose) verbose=1 ; shift ;;
        -t|--test) testname=$2 ; shift 2 ;;
        -n|--num) number=$2 ; shift 2 ;;
        --contest) contest_slug=$2; shift 2 ;;
        --) shift ; break ;;
    esac
done

set_colors

# alternate syntax
if [ -z "${testname}" ]; then
    testname=$1
    [ -z "${testname}" ] && usage 3
fi

# testcase file must exist
[ -f "${testname}" ] || usage 4

# for batch processing
close_std

# extract the extension
extension="${testname##*.}"
if [ "${extension}" == "py" ]; then
    exe="python3 ${testname}"
    testname="${testname%.*}"
else
    exe=./${testname}
fi

testcases="${rootdir}/testcases/${testname}-testcases.zip"
testcases2="${rootdir}/testcases2/${testname}-testcases2.zip"

download_pdf
download_zip

mkdir -p tests
unzip -q -o -d tests/${testname} "${testcases}" 2>/dev/null
if [ $? -ne 0 ]; then
    grep -q "testcases are not available for download"  "${testcases}" && {
        echo SKIPPED
        exit 0
    }
fi

if [ ! -z "$number" -a -s "${testcases2}" ]; then
    unzip -q -o -d tests/${testname} "${testcases2}"
fi

if [ $verbose ]; then
    /bin/ls -ogTp tests/${testname}/input/
fi

failure=0
for input in tests/${testname}/input/input*.txt; do
    n=${input##*input}

    if [ ! -z "$number" ]; then
        if [ "$number" -ne "${n%%.txt}" ]; then
            continue
        fi
    fi

    echo -e "${COLOR_YELLOW}${exe} < ${input}${COLOR_END}"
    ${exe} < ${input} | tee tests/$testname/result${n}
    echo -ne "${COLOR_PURPLE}"
    compare tests/$testname/result${n} tests/$testname/output/output${n}
    rc=$?
    echo -ne "${COLOR_END}"
    [ $rc -ne 0 ] && failure=1
    if [ $rc -eq 0 ] ; then
        echo -e "${COLOR_YELLOW}TESTCASE ${n%%.txt} : ${COLOR_GREEN}SUCCESS${COLOR_END}"
    else
        echo -e "${COLOR_YELLOW}TESTCASE ${n%%.txt} : ${COLOR_RED}FAILURE${COLOR_END}"
    fi
    echo
done

if [ $failure -eq 0 ] ; then
    echo -e "${COLOR_GREEN}SUCCESS${COLOR_END}"
else
    echo -e "${COLOR_RED}FAILURE${COLOR_END}"
fi
exit $failure
