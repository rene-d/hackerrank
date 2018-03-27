# build and test HackerRank solutions

cmake_minimum_required(VERSION 3.5)

set (CMAKE_MODULE_PATH "${CMAKE_MODULE_PATH};${CMAKE_SOURCE_DIR}/cmake-haskell/cmake")

project(hackerrank)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_FLAGS "-Wall -Wextra -Wconversion")
set(CMAKE_C_FLAGS "-std=c99 -Wall -Wextra -Wconversion")

enable_testing()

set(HACKERRANK_MASTER)
macro(add_test_hackerrank name)
    add_test(NAME ${name}
             COMMAND ${CMAKE_SOURCE_DIR}/runtest.sh ${name} ${HACKERRANK_MASTER}
             WORKING_DIRECTORY ${CURRENT_BINARY_DIR})
endmacro()

macro(add_hackerrank name cpp)
    add_executable("${name}" "${cpp}" ${ARGV})
    add_test_hackerrank(${name})
endmacro(add_hackerrank name cpp)

macro(add_hackerrank_py name)
    configure_file("${name}" "${name}" COPYONLY)
    add_test_hackerrank(${name})
endmacro(add_hackerrank_py nae)


# C++
add_subdirectory("cpp")

# Python
add_subdirectory("python")

# Mathematics
add_subdirectory("math")

# Algo
add_subdirectory("algo")

# Data Structures
add_subdirectory("data")

# Project Euler+
add_subdirectory("projecteuler")

add_subdirectory("fp")
