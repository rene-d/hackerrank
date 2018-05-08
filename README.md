# [![HackerRank](https://hrcdn.net/hackerrank/assets/brand/h_mark_sm-30dc0e0cbd2dded63b294819ff853a90.svg)](https://www.hackerrank.com) HackerRank

[![Build Status](https://travis-ci.org/rene-d/hackerrank.svg?branch=master)](https://travis-ci.org/rene-d/hackerrank) [![529 solutions and counting](https://img.shields.io/badge/Challenges-529-blue.svg)](https://github.com/rene-d/hackerrank)

[HackerRank](https://www.hackerrank.com/dashboard) is a great site to learn, improve, play with your programming skills.

## Solutions

[![C++](https://hrcdn.net/hackerrank/assets/dashboard/cpp-4644489c8b8e68a81dd0ccfac5097c2e.svg)](cpp/)
[![Python](https://hrcdn.net/hackerrank/assets/dashboard/python-473706315bc214a540c1ca7b57f60854.svg)](python/)
[![Shell](https://hrcdn.net/hackerrank/assets/dashboard/shell-5c42f1aa41f72148347b7e91bf46ae4f.svg)](shell/)
[![Algorithms](https://hrcdn.net/hackerrank/assets/dashboard/algorithms-ea9e958ddb5b097c5ebcdd22de4a9766.svg)](algorithms/)
[![Data Structures](https://hrcdn.net/hackerrank/assets/dashboard/data-structures-e83daf9e8769351037cc25ff131931d1.svg)](data-structures/)
[![Mathematics](https://hrcdn.net/hackerrank/assets/dashboard/mathematics-3ec234bd89020880ff0349f9cacdab30.svg)](mathematics/)
[![30 Days of Code](https://hrcdn.net/hackerrank/assets/dashboard/30-days-of-code-bf00cb8a1c6f38bf917f45ea7ab2bf6b.svg)](tutorials/30-days-of-code/)
[![Cracking the Coding Interview](https://hrcdn.net/hackerrank/assets/dashboard/cracking-the-coding-interview-a56b2213a9c4f9393bfeb13261449c37.svg)](tutorials/cracking-the-coding-interview/)

and [ProjectEuler+](contests/projecteuler/) (See [here](https://github.com/rene-d/math/tree/master/projecteuler) my solutions of [Project Euler](https://projecteuler.net/))

## Usage and tools

### Requirements

- [Python 3.6](https://www.python.org) and some libraries ([numpy](http://www.numpy.org), [requests](http://html.python-requests.org)), [flake8](http://flake8.readthedocs.io/)
- [CMake](https://cmake.org)
- Modern gcc or clang that come with macOS or Linux. Under Windows, use [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) or [MinGW](http://www.mingw.org).
- [Haskell](https://www.haskell.org) (functional programming only)

### Compilation

    mkdir build
    cd build
    cmake ..
    make

### Tests

    cd build
    make extract-testcases
    ctest [-R filter]

It will download the challenge testcases and run solution programs.

A solution can be tested solely with `runtest.sh -t challenge-name [-n test-number]` in its build subdirectory.

### Tools

- `hrinit.py` creates a new file for a given challenge based on the HackerRank model. Default language is [Python 3](https://wiki.python.org/moin/Python2orPython3).

- `runtest.sh` is the script used by [CTest](https://cmake.org/Wiki/CMake/Testing_With_CTest) to verify the solution.

- `compare.py` aims to fairly compare the program output with the except one. It is necessary since some challenges use decimal numbers : we cannot simply use `diff -qw`.

- `tc2.py` can be used to download purchased testcases. Copy and paste the download link.

- `hackos.py` lists the free testcases. It should be used in conjunction with a webbrowser. Follow instructions in the source code.

### IDE

[Visual Studio Code](https://code.visualstudio.com) is a great free IDE that comes with many [plugins](https://marketplace.visualstudio.com/vscode). Some configuration files are provided.
