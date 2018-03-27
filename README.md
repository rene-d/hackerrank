# [![HackeRank](https://hrcdn.net/hackerrank/assets/brand/h_mark_sm-30dc0e0cbd2dded63b294819ff853a90.svg)](https://www.hackerrank.com) HackerRank

HackerRank is a great site to learn, improve, play with programming skills.

    ===============================================================================
    ,--.  ,--.              ,--.                 ,------.                 ,--.
    |  '--'  | ,--,--. ,---.|  |,-. ,---. ,--.--.|  .--. ' ,--,--.,--,--, |  |,-.
    |  .--.  |' ,-.  || .--'|     /| .-. :|  .--'|  '--'.'' ,-.  ||      \|     /
    |  |  |  |\ '-'  |\ `--.|  \  \\   --.|  |   |  |\  \ \ '-'  ||  ||  ||  \  \
    `--'  `--' `--`--' `---'`--'`--'`----'`--'   `--' '--' `--`--'`--''--'`--'`--'
    ===============================================================================

## Solutions

### [C++](https://www.hackerrank.com/domains/cpp)

### [Python](https://www.hackerrank.com/domains/python)

### [Mathematics](https://www.hackerrank.com/domains/mathematics)

### [Algorithms](https://www.hackerrank.com/domains/algorithms)

### [Data Structures](https://www.hackerrank.com/domains/data-structures)

### [ProjectEuler+](https://www.hackerrank.com/contests/projecteuler/challenges)

## Usage and tools

### Compilation

    mkdir build
    cd build
    cmake ..
    make
    
### Tests

    cd build
    cd algo
    ctest [-R filter]

It will download the challenge testcase and runs the solution with it.

### Tools

`init.py` creates a new file for a given challenge based on the template

`runtest.sh` is the script used by CTest to run tests on a challenge.

`compare.py` aims to fairly compare the program output with the except one. It is necessary since some challenges use decimal numbers.

`tc2.py` can be used to download bought testcases. Copy and paste the download link.

`hackos.py` lists the free testcases. It requires a webbrowser.

