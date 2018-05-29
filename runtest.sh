#!/bin/bash
#set -x
#echo $* >> runtest-cmdline.txt

# program parameters
rootdir=$(dirname "$0")
contest=master
quiet=
number=                     # testcase number (default 0)
testsdir=                   # path for testcases files (<tests>/<contest>/<challenges>/input/...)
extract_tests=

# program usage
usage()
{
    echo "Usage: runtest.sh [options]"
    echo "  -h,--help       : help"
    echo "  -t,--testcase   : testcase name"
    echo "  -n,--number     : testcase number"
    exit $1
}

# colors for term
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

##############################################################################

# read the options
if [ "$(uname)" = "Darwin" ]; then
    ARGS=`getopt hqc:t:n:T:X: $*`
else
    ARGS=`getopt -o hqc:t:n:T:X: --long help,quiet,contest:,test:,number: -n 'runtest.sh' -- "$@"`
fi
eval set -- "$ARGS"
[ $? != 0 ] && usage 2

# extract options and their arguments into variables.
for i ; do
    case "$i" in
        -h|--help) usage ;;
        -q|--quiet) quiet=1 ; shift ;;
        -c|--contest) contest=$2 ; shift 2 ;;
        -t|--test) testname=$2 ; shift 2 ;;
        -n|--number) number=$2 ; shift 2 ;;
        -T) testsdir=$2 ; shift 2 ;;
        -X) extract_tests=$2 ; shift 2;;
        --) shift ; break ;;
    esac
done

if [ $extract_tests ]; then
    if [ -s "${rootdir}/testcases.tar.xz" ]; then
        mkdir -p "${extract_tests}"
        tar -C "${extract_tests}" -xJf "${rootdir}/testcases.tar.xz"
        exit $?
    fi
    exit 1
fi

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
    result=result${extension}
elif [ "${extension}" == "sh" ]; then
    exe="bash ${testname}"
    testname="${testname%.*}"
    result=result${extension}
elif [ "${extension}" == "jar" ]; then
    exe="java -jar ${testname}"
    testname="${testname%.*}"
    result=result${extension}
else
    exe=./${testname}
    result=result-${testname}
    # special case for duplicated challenges (practice/contest)
    testname=${testname%_*}
fi

##############################################################################

# trois considérations:
#   - le répertoire <tests>/<testname>/input/ existe
#   - le fichier <rootdir>/testcases/<contest>/<testname>-testcases.zip
#   - le fichier <rootdir>/testcases2/<contest>/<testname>-testcases2.zip

if [ "${testsdir}" != "" -a -d "${testsdir}/${contest}/${testname}" ]; then
    testsdir="${testsdir}/${contest}"
else
    testsdir=tests
    mkdir -p tests

    # si les fichiers de testcases existent: on les extrait
    zip="${rootdir}/testcases/${contest}/${testname}-testcases.zip"
    if [ -s "${zip}" ]; then
        unzip -q -o -d tests/${testname} "${zip}"
    fi

    zip="${rootdir}/testcases2/${contest}/${testname}-testcases2.zip"
    if [ -s "${zip}" ]; then
        unzip -q -o -d tests/${testname} "${zip}"
    fi

    zip="${rootdir}/offline/testcases/${contest}/${testname}-testcases.zip"
    if [ -s "${zip}" ]; then
        unzip -q -o -d tests/${testname} "${zip}"
    fi
fi

# si on n'a pas le répertoire des testcases, c'est une erreur
if [ ! -d "${testsdir}/${testname}/input" ]; then
    echo -e "${COLOR_RED}MISSING TESTCASES${COLOR_END}"
    exit 1
fi

##############################################################################


failure=0
for input in "${testsdir}/${testname}/input/input"*.txt; do
    n=${input##*input}

    if [ ! -z "$number" -a "$number" != "a" ]; then
        if [ "$number" -ne "${n%%.txt}" ]; then
            continue
        fi
    fi

    echo -e "${COLOR_YELLOW}${exe} < ${input}${COLOR_END}"
    if [ $quiet ]; then
        ${exe} < "${input}" > "${testsdir}/$testname/${result}${n}"
    else
        ${exe} < "${input}" | tee "${testsdir}/$testname/${result}${n}"
    fi

    echo -ne "${COLOR_PURPLE}"
    compare "${testsdir}/$testname/${result}${n}" "${testsdir}/$testname/output/output${n}"
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
