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
        COLOR_CYAN="\033[0;36m"
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
elif [ "${extension}" == "js" ]; then
    exe="node ${testname}"
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
#   - le fichier <rootdir>/testcases2/<contest>/<testname>-testcases.zip

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

    zip="${rootdir}/testcases2/${contest}/${testname}-testcases.zip"
    if [ -s "${zip}" ]; then
        unzip -q -o -d tests/${testname} "${zip}"
    fi

    zip="${rootdir}/offline/testcases/${contest}/${testname}-testcases.zip"
    if [ -s "${zip}" ]; then
        unzip -q -o -d tests/${testname} "${zip}"
    fi
fi

# the root folder for inputs, outputs and results
testdir=${testsdir}/${testname}

# si on n'a pas le répertoire des testcases, c'est une erreur
if [ ! -d "${testdir}/input" ]; then
    echo -e "${COLOR_RED}MISSING TESTCASES${COLOR_END}"
    exit 1
fi

##############################################################################

failure=0
for input in "${testdir}/input/input"*.txt; do
    n=${input##*input}
    n=${n%%.txt}

    if [ ! -z "$number" -a "$number" != "a" ]; then
        if [ "$number" -ne "${n}" ]; then
            continue
        fi
    fi

    echo -e "${COLOR_YELLOW}${exe} < ${input}${COLOR_END}"

    exec 3>&2                                   # fd 3 is stderr too
    exec 2> "${testdir}/${result}${n}.time"     # builtin time will write to a file, not stderr
    TIMEFORMAT="${COLOR_CYAN}(real %2R user %2U sys %2S)${COLOR_END}"

    # old templates use the environment variable OUTPUT_PATH
    export OUTPUT_PATH=/dev/stdout

    if [ $quiet ]; then
        time ${exe} < "${input}" 2>&3 > "${testdir}/${result}${n}.txt"
    else
        time ${exe} < "${input}" 2>&3 | tee "${testdir}/${result}${n}.txt"
    fi

    exec 2>&3       # restore stderr
    exec 3<&-       # close fd 3
    elapsed=$(< ${testdir}/${result}${n}.time)

    echo -ne "${COLOR_PURPLE}"
    compare "${testdir}/${result}${n}.txt" "${testdir}/output/output${n}.txt"
    rc=$?
    echo -ne "${COLOR_END}"
    [ $rc -ne 0 ] && failure=1
    if [ $rc -eq 0 ] ; then
        echo -e "${COLOR_YELLOW}TESTCASE ${n} : ${COLOR_GREEN}SUCCESS${COLOR_END} ${elapsed}"
    else
        echo -e "${COLOR_YELLOW}TESTCASE ${n} : ${COLOR_RED}FAILURE${COLOR_END} ${elapsed}"
    fi
    echo
done

if [ $failure -eq 0 ] ; then
    echo -e "${COLOR_GREEN}SUCCESS${COLOR_END}"
else
    echo -e "${COLOR_RED}FAILURE${COLOR_END}"
fi
exit $failure
