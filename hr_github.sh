#! /bin/bash

# update testcases archive and sync GitHub repo

which -s python3 || { echo "Missing Python3"; exit 2; }

cwd="$(cd $(dirname $0); pwd)"
cd "${cwd}"

GITHUB_REPO=../GitHub/hackerrank

DOMAINS=($(python3 -c 'import yaml;print(*yaml.load(open(".hr_conf.yaml"))["domains"])'))

COLOR_LIGHT_PURPLE="\033[1;35m"
COLOR_END="\033[0m"


cmd_testcases_archive()
{
    echo -e "${COLOR_LIGHT_PURPLE}Preparing testcases...${COLOR_END}"

    rm -rf tmp

    for i in testcases/*/*-testcases.zip ; do
        contest=$(basename $(dirname $i))
        mkdir -p tmp/$contest

        if [ $contest = master ]; then
            unzip -q -o -d tmp/$contest/$(basename $i -testcases.zip) $i
            if [ $? -eq 0 ]; then
                echo -n .
            else
                echo -n X
            fi
        else
            # les contests ont l'ensemble des testcases: trop gros !
            unzip -q -o -d tmp/$contest/$(basename $i -testcases.zip) $i input/input00.txt output/output00.txt 2>/dev/null
            if [ $? -ne 0 ]; then
                # mais pas toujours le testcase 00...
                unzip -q -o -d tmp/$contest/$(basename $i -testcases.zip) $i
                if [ $? -eq 0 ]; then
                    echo -n 2
                else
                    echo -n Y
                fi
            else
                echo -n 1
            fi
        fi
    done

    # s'il manque des testcases, on les cherche dans la version "achetée"
    for i in testcases/*/*-testcases.err ; do
        contest=$(basename $(dirname $i))
        mkdir -p tmp/$contest
        t=testcases2/$contest/$(basename $i .err).zip
        if [ -f $t ]; then
            unzip -q -o -d tmp/$contest/$(basename $i -testcases.err) $t
            echo -n .
        else
            echo
            echo "No testcase for $t"
        fi
    done

    # ajoute les testcases supplémentaires
    # for i in testcases_extra/*/*-testcases.zip ; do
    #     contest=$(basename $(dirname $i))
    #     mkdir -p tmp/$contest
    #     unzip -q -o -d tmp/$contest/$(basename $i -testcases.zip) $i
    #     if [ $? -eq 0 ]; then
    #         echo -n 3
    #     else
    #         echo -n Z
    #     fi
    # done

    echo
    echo -e "${COLOR_LIGHT_PURPLE}Generating testcases archive...${COLOR_END}"

    find tmp -name "*.txt" | cut  -b5- | xargs tar -C tmp -cJf testcases.tar.xz
    count=$(($(ls -d tmp/*/* | wc -l)))
    rm -rf tmp

    echo "  testcases count: $count"
}


cmd_count()
{
    echo -e "${COLOR_LIGHT_PURPLE}Counting...${COLOR_END}"
    counts=($(python3 hr_count.py $@))
    echo "  challenges: ${counts[0]} (unique)"
    echo "  challenges: ${counts[1]} (overall)"
    echo "  solutions: ${counts[2]} (for all languages)"
    #echo "  solutions: ${counts[3]} (overall)"
    challenges=${counts[0]}
    sed  -e "s/[[:digit:]]*\( solutions and counting\)/"$challenges"\1/" \
         -e "s/\(Challenges\-\)[[:digit:]]*\(-blue\)/\1"$challenges"\2/" README.md > README.md.tmp
    if diff -qs README.md README.md.tmp > /dev/null;  then
        rm README.md.tmp
    else
        echo  "  rewrite README.md"
        mv -f README.md.tmp README.md
    fi
}


cmd_readme()
{
    echo -e "${COLOR_LIGHT_PURPLE}Generating README...${COLOR_END}"
    python3 ./hr_table.py
}


cmd_build_test()
{
    echo -e "${COLOR_LIGHT_PURPLE}Build and test...${COLOR_END}"

    if [ $(uname) = Darwin ] ; then
        nproc()
        {
            sysctl -n hw.logicalcpu
        }
    fi

    (
        cd "${cwd}"
        gh_src="$(cd ${GITHUB_REPO}; pwd)"
        mkdir -p build/github
        cd build/github
        cmake -DHACKERRANK_FP:BOOL=OFF -DCMAKE_BUILD_TYPE=Release "${gh_src}"
        make -j$(nproc)
        make extract-testcases
        ctest -j$(nproc) --output-on-failure
    )
}


cmd_rsync()
{
    echo -e "${COLOR_LIGHT_PURPLE}Rsync...${COLOR_END}"
    # copie les fichiers vers le dépôt GitHub
    rsync -av --delete --exclude .DS_Store --exclude="*.tmp" --exclude="*.nosync" --exclude="tests" \
        ${DOMAINS[*]} \
        coding-dojo \
        .vscode CMakeLists.txt requirements.txt README.md stdc++.h.in runtest.sh compare.py hrinit.py hrtc2.py \
        testcases.tar.xz \
        setup.cfg \
        .travis.yml _config.yml \
        hr_count.py  hr_github.sh hr_interview.py hr_offline.py hr_table.py Makefile .hr_conf.yaml \
        hr_db.py hr_menu.py \
        ${GITHUB_REPO}
}


cmd_usage()
{
    echo "Usage: $0 [options]"
    echo "  -h      help"
    echo "  -t      make testcases archive"
    echo "  -b      build and run tests"
    echo "  -T      make archive then build and test"
    exit 0
}


ARGS=`getopt htbTX: $*`
eval set -- "$ARGS"
[ $? != 0 ] && usage 2

opt_archive=
opt_build=

# extract options and their arguments into variables.
for i ; do
    case "$i" in
        -h|--help) cmd_usage ;;
        -t) opt_archive=1 ; shift ;;
        -b) opt_build=1 ; shift ;;
        -T) opt_archive=1 ; opt_build=1 ; shift ;;
        -X) shift; $1 ; exit 0 ;;   # run individual command
    esac
done

cmd_readme
cmd_count ${DOMAINS[*]}
[ $opt_archive ] && cmd_testcases_archive
cmd_rsync
[ $opt_build ] && cmd_build_test
echo
