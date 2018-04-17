#!/bin/bash
#set -x
#echo $* >> runtest-cmdline.txt

# program parameters
rootdir=$(dirname "$0")
verbose=
number=
contest_slug=master
testcase=
download=
quiet=

# program usage
usage()
{
    echo "Usage: runtest.sh [options]"
    echo "  -h,--help       : help"
    echo "  -t,--testcase   : testcase name"
    echo "  -n,--number     : testcase number"
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

    # download only if directory statements exists
    #[ -d "${rootdir}/statements" ] || return

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
    [ -f "${testcases%%.zip}.err" ] && return
    [ -s "${testcases}" ] && return

    mkdir -p "${rootdir}/testcases"

    url="https://www.hackerrank.com/rest/contests/${contest_slug}/challenges/${testname}/download_testcases"
    http_code=$(curl --write-out %{http_code} -s -L -o "${testcases}" "${url}")

    if [ $http_code -ne 200 ]; then
        if [ -f "${testcases}" ]; then
            mv -f "${testcases}" "${testcases%%.zip}.err"
        fi
        echo "Download problem: ${url}"
    fi
}

# read the options
if [ "$(uname)" = "Darwin" ]; then
    ARGS=`getopt hvn:t:c:aDq $*`
else
    ARGS=`getopt -o hvn:t:c:aDq --long help,verbose,contest:,number:,test:,all,download,quiet -n 'runtest.sh' -- "$@"`
fi
eval set -- "$ARGS"
[ $? != 0 ] && usage 2

# extract options and their arguments into variables.
for i ; do
    case "$i" in
        -h|--help) usage ;;
        -q|--quiet) quiet=1 ; shift ;;
        -v|--verbose) verbose=1 ; shift ;;
        -D|--download) download=1; shift ;;
        -t|--test) testname=$2 ; shift 2 ;;
        -n|--num) number=$2 ; shift 2 ;;
        -a|--all) number=a ; shift ;;
        -c|--contest) contest_slug=$2; shift 2 ;;
        --) shift ; break ;;
    esac
done

# alternate syntax
if [ -z "${testname}" ]; then
    testname=$1
    [ -z "${testname}" ] && usage 3
fi

# testcase file must exist
[ -f "${testname}" ] || usage 4

# for batch/interactive processing
set_colors
close_std

# extract the extension
extension="${testname##*.}"
if [ "${extension}" == "py" ]; then
    exe="python3 ${testname}"
    testname="${testname%.*}"
elif [ "${extension}" == "sh" ]; then
    exe="bash ${testname}"
    testname="${testname%.*}"
else
    exe=./${testname}
fi

testcases="${rootdir}/testcases/${testname}-testcases.zip"
testcases2="${rootdir}/testcases2/${testname}-testcases2.zip"

if [ $download ]; then
    echo "Downloading testcases..."
    #download_pdf
    download_zip
fi

mkdir -p tests

if [ -f  "${testcases}" ]; then
    unzip -q -o -d tests/${testname} "${testcases}"
    missing_testcases=0
else
    missing_testcases=1
fi

if [ \( ! -z "$number" -o $missing_testcases -eq 1 \) -a -s "${testcases2}" ]; then
    unzip -q -o -d tests/${testname} "${testcases2}"
fi

if [ $missing_testcases -eq 1 ]; then
    tar -C tests -xJvf "${rootdir}/testcases.tar.xz" ${testname}
fi

if [ ! -d tests/${testname}/input ]; then
    echo -e "${COLOR_RED}NO TEST${COLOR_END}"
    exit 1
fi

if [ $verbose ]; then
    /bin/ls -ogTp tests/${testname}/input/
fi

failure=0
for input in tests/${testname}/input/input*.txt; do
    n=${input##*input}

    if [ ! -z "$number" -a "$number" != "a" ]; then
        if [ "$number" -ne "${n%%.txt}" ]; then
            continue
        fi
    fi

    echo -e "${COLOR_YELLOW}${exe} < ${input}${COLOR_END}"
    if [ $quiet ]; then
        ${exe} < ${input} > tests/$testname/result${n}
    else
        ${exe} < ${input} | tee tests/$testname/result${n}
    fi
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
