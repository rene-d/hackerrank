# build and test HackerRank solutions
#

cmake_minimum_required(VERSION 3.5)

option(HACKERRANK_FP "Toggle Functional Programming" OFF)

if(HACKERRANK_FP)
    set(CMAKE_MODULE_PATH "${CMAKE_MODULE_PATH};${CMAKE_SOURCE_DIR}/cmake-haskell/cmake")
endif()

project(hackerrank)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_FLAGS "-Wall -Wextra -Wconversion -Werror")
set(CMAKE_C_FLAGS "-std=c99 -Wall -Wextra -Wconversion -Werror")

if(CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    # clang n'a pas le fichier pratique de gcc de précompilation des headers de la STL
    configure_file(stdc++.h.in bits/stdc++.h COPYONLY @ONLY)
    include_directories(${CMAKE_CURRENT_BINARY_DIR})
endif()

# installe un fichier .nosync pour éviter la synchro iCloud Drive
if(NOT EXISTS "${CMAKE_CURRENT_BINARY_DIR}/iCloud.nosync")
  file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/iCloud.nosync" "build dir\n${CMAKE_SYSTEM}\n${CMAKE_SYSTEM_PROCESSOR}\n")
endif()

enable_testing()

set(HACKERRANK_CONTEST_SLUG master)
macro(add_test_hackerrank name)
    add_test(NAME ${name}
             COMMAND ${CMAKE_SOURCE_DIR}/runtest.sh -t ${name} -c ${HACKERRANK_CONTEST_SLUG}
             WORKING_DIRECTORY ${CURRENT_BINARY_DIR})
endmacro()

macro(add_hackerrank name cpp)
    add_executable("${name}" "${cpp}" ${ARGV})
    add_test_hackerrank(${name})
endmacro(add_hackerrank name cpp)

# les auteurs d'hackerrank n'assoient un peu sur la qualité de leur code
macro(dirty_cpp name)
    target_compile_options("${name}" PRIVATE "-Wno-sign-compare")
    target_compile_options("${name}" PRIVATE "-Wno-sign-conversion")
    target_compile_options("${name}" PRIVATE "-Wno-sign-conversion")
    target_compile_options("${name}" PRIVATE "-Wno-shorten-64-to-32")
    target_compile_options("${name}" PRIVATE "-Wno-unused-parameter")
    target_compile_options("${name}" PRIVATE "-Wno-reorder")
endmacro(dirty_cpp name)

macro(add_hackerrank_py name)
    configure_file("${name}" "${name}" COPYONLY @ONLY)
    add_test_hackerrank(${name})
endmacro(add_hackerrank_py name)

macro(add_hackerrank_shell name)
    configure_file("${name}" "${name}" COPYONLY @ONLY)
    add_test_hackerrank(${name})
endmacro(add_hackerrank_shell name)


add_subdirectory(cpp)
add_subdirectory(python)
add_subdirectory(mathematics)
add_subdirectory(algorithms)
add_subdirectory(data-structures)
add_subdirectory(projecteuler)
add_subdirectory(tutorials)
add_subdirectory(shell)
add_subdirectory(contests)

if(HACKERRANK_FP)
    add_subdirectory(fp)
endif()