# [![HackerRank](https://hrcdn.net/hackerrank/assets/brand/h_mark_sm-30dc0e0cbd2dded63b294819ff853a90.svg)](https://www.hackerrank.com) HackerRank

[![Build Status](https://travis-ci.org/rene-d/hackerrank.svg?branch=master)](https://travis-ci.org/rene-d/hackerrank) [![809 solutions and counting](https://img.shields.io/badge/Challenges-809-blue.svg)](https://www.hackerrank.com/rene_d?hr_r=1)

[HackerRank](https://www.hackerrank.com/dashboard) is a great place to learn, improve, play with your programming skills.

All challenges are runnable, except SQL and multiple choice question ones. They are verified with their default testcase (usually Testcase 0).


## Solutions

[![C++](https://hrcdn.net/hackerrank/assets/dashboard/cpp-4644489c8b8e68a81dd0ccfac5097c2e.svg)](cpp/)
<a href="c/"><img src="https://hrcdn.net/hackerrank/assets/dashboard/c-43bbd380e51d62b83c4b542c58699a97.svg" width="50px" height="50px"></a>
[![Python](https://hrcdn.net/hackerrank/assets/dashboard/python-473706315bc214a540c1ca7b57f60854.svg)](python/)
[![Shell](https://hrcdn.net/hackerrank/assets/dashboard/shell-5c42f1aa41f72148347b7e91bf46ae4f.svg)](shell/)
[![Java](https://hrcdn.net/hackerrank/assets/dashboard/java-5a95cc68f65be63c24f5913e29bafb66.svg)](java/)
&nbsp;&nbsp;&nbsp;
[![Algorithms](https://hrcdn.net/hackerrank/assets/dashboard/algorithms-ea9e958ddb5b097c5ebcdd22de4a9766.svg)](algorithms/)
[![Data Structures](https://hrcdn.net/hackerrank/assets/dashboard/data-structures-e83daf9e8769351037cc25ff131931d1.svg)](data-structures/)
[![Mathematics](https://hrcdn.net/hackerrank/assets/dashboard/mathematics-3ec234bd89020880ff0349f9cacdab30.svg)](mathematics/)

[![30 Days of Code](https://hrcdn.net/hackerrank/assets/dashboard/30-days-of-code-bf00cb8a1c6f38bf917f45ea7ab2bf6b.svg)](tutorials/30-days-of-code/)
[![Cracking the Coding Interview](https://hrcdn.net/hackerrank/assets/dashboard/cracking-the-coding-interview-a56b2213a9c4f9393bfeb13261449c37.svg)](tutorials/cracking-the-coding-interview/)
[![10 Days of Statistics](https://hrcdn.net/hackerrank/assets/dashboard/10-days-of-statistics-f45c998a5d47c9527eb61e620f35f5c0.svg)](tutorials/10-days-of-statistics/)
[![10 Days of Javascript](https://hrcdn.net/hackerrank/assets/dashboard/10-days-of-javascript-bf50d09114e28b603041e791559003b6.svg)](tutorials/10-days-of-javascript/)
&nbsp;&nbsp;&nbsp;
[![Regex](https://hrcdn.net/hackerrank/assets/dashboard/regex-d83b1db79fe03650410202032d3b8afd.svg)](regex/)
[![Security](https://hrcdn.net/hackerrank/assets/dashboard/security-ee10c8f654e78f4659d5dc6305768a63.svg)](security/)
[![Databases](https://hrcdn.net/hackerrank/assets/dashboard/databases-0ff7fcc96c1e9516abc9ea327c9a0ef9.svg)](databases/)
[![SQL](https://hrcdn.net/hackerrank/assets/dashboard/sql-be1ac821f4358a522d8eba7600e69549.svg)](sql/)

The curated challenges of [Interview Preparation Kit](interview-preparation-kit/).

And [ProjectEuler+](contests/projecteuler/) (See [here](https://github.com/rene-d/math/tree/master/projecteuler) my solutions of [Project Euler](https://projecteuler.net/))

## Usage and tools

### Requirements

- [Python 3.6 or 3.7](https://www.python.org) and some packages : [numpy](http://www.numpy.org), [SciPy](https://www.scipy.org), [scikit-learn](http://scikit-learn.org/), [requests](http://html.python-requests.org), [flake8](http://flake8.readthedocs.io/), [PyYAML](https://pyyaml.org)
- [CMake](https://cmake.org) to build and run tests
- Modern [GCC](https://gcc.gnu.org) or [Clang](https://clang.llvm.org) that comes    with macOS or Linux. For Windows, you can use [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10), [Cygwin](https://www.cygwin.com) or [Visual Studio Comunity 2017](https://www.visualstudio.com/downloads/)
- [Haskell](https://www.haskell.org) (functional programming only)
- [Java](http://www.oracle.com/technetwork/java/javase/index.html) (some challenges and Java practice)
- [Node.js](https://nodejs.org/)

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

- `hrinit.py` creates a new file for a given challenge based on the HackerRank template. Default choice for language is [Python 3](https://wiki.python.org/moin/Python2orPython3).
- `runtest.sh` is the script used by [CTest](https://cmake.org/Wiki/CMake/Testing_With_CTest) to verify the solution.
- `compare.py` aims to fairly compare the program output with the excepted one. It is necessary since some challenges use decimal numbers : we cannot simply use `diff -qw`.
- `hrtc2.py` can be used to download «purchased» testcases or to create new ones. Copy and paste the download links of input and output data.

### Other (hacking) tools

- `hr_github.sh` creates the testcases archive and sync the private repo to the public GitHub one
- `hr_table.py` automatically creates `README.md` files with challenge lists (requires offline data)
- `hr_count.py` counts challenges and testcases - used to update toplevel `README.md`
- `hr_offline.py` downloads challenge catalogs and more
- `hr_interview.py` gets the playlist of [Interview Preparation Kit](https://www.hackerrank.com/interview/interview-preparation-kit)
- `hr_menu.py` displays a graphical menu to browse challenges and solve them when no Internet connection is available (requires offline data)
- `hr_db.py` creates a SQLite database - used to understand how data is structured (or not!)

### IDE

[Visual Studio Code](https://code.visualstudio.com) is a great free IDE that comes with many [plugins](https://marketplace.visualstudio.com/vscode). Some configuration files are provided and a [Bash](https://www.gnu.org/software/bash/) initialization file.

### Other online resources

* [stack overflow](https://stackoverflow.com) and [Mathematics Stack Exchange](https://math.stackexchange.com)
* [GeeksforGeeks](https://www.geeksforgeeks.org) Computer Science portal and resources
* [Rosetta Code](http://rosettacode.org/wiki/Rosetta_Code)
* [tutorialspoint](https://www.tutorialspoint.com/)
* [Compiler Explorer](https://godbolt.org) Run compilers interactively from your web browser and interact with the assembly ([opensource](https://github.com/mattgodbolt/compiler-explorer)).
* [Ideone](https://ideone.com) Online compiler and debugging tool which allows youto compile source code and execute it online in more than 60 programming languages.
* and many, many more...

## License

[Unlicense](http://unlicense.org) aka. Public Domain &#x1F918;
