# [![HackeRank](https://hrcdn.net/hackerrank/assets/brand/h_mark_sm-30dc0e0cbd2dded63b294819ff853a90.svg)](https://www.hackerrank.com) HackerRank

HackerRank is a great site to learn, improve, play with your programming skills.

## Solutions

* [C++](cpp/)
* [Python](python/)
* [Mathematics](math/)
* [Algorithms](algo/)
* [Data Structures](data/)
* [ProjectEuler+](projecteuler/) (See [here](https://github.com/rene-d/math/tree/master/projecteuler) my solutions to [Project Euler](https://projecteuler.net/))

## Usage and tools

### Requirements

- [Python 3.6](https://www.python.org) and some libraries ([numpy](http://www.numpy.org), [requests](http://html.python-requests.org))
- [CMake](https://cmake.org)
- Modern gcc or clang

### Compilation

    mkdir build
    cd build
    cmake ..
    make

### Tests

    cd build
    ctest [-R filter]

It will download the challenge testcases and run solution programs.

### Tools

- `init.py` creates a new file for a given challenge based on the HackerRank template

- `runtest.sh` is the script used by CTest to run the solution.

- `compare.py` aims to fairly compare the program output with the except one. It is necessary since some challenges use decimal numbers : we cannot simply use `diff -qw`.

- `tc2.py` can be used to download bought testcases. Copy and paste the download link.

- `hackos.py` lists the free testcases. It requires a webbrowser. Follow instructions in the source code.

