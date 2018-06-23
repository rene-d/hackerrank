# Build and test HackerRank solutions
#

cmake_minimum_required(VERSION 3.5)

project(hackerrank)


#
# Options
#

option(HACKERRANK_FP "Toggle Functional Programming" OFF)
option(HACKERRANK_JAVA "Toggle Java" ON)
option(HACKERRANK_JS "Toggle Javascript (Node.js)" ON)


#
# Check environment
#

if(HACKERRANK_JAVA)
    find_program(JAVAC_BIN javac DOC "path to Java compiler")
    if(NOT JAVAC_BIN)
        set(HACKERRANK_JAVA OFF)
        message(WARNING "Disabling Java: compiler not found")
    else()
        #message(STATUS "Java compiler: ${JAVAC_BIN}")
    endif()
endif()

if(HACKERRANK_JS)
    find_program(NODEJS_BIN node DOC "path to Node.js runtime")
    if(NOT NODEJS_BIN)
        set(HACKERRANK_JS OFF)
        message(WARNING "Disabling Node.js: runtime not found")
    else()
        #message(STATUS "Node.js runtime: ${NODEJS_BIN}")
    endif()
endif()


#
# Compilation settings
#

set(CMAKE_EXPORT_COMPILE_COMMANDS on)

if(HACKERRANK_FP)
    set(CMAKE_MODULE_PATH "${CMAKE_MODULE_PATH};${CMAKE_SOURCE_DIR}/cmake-haskell/cmake")
endif()

if(HACKERRANK_JAVA)
    find_package(Java REQUIRED)
    include(UseJava)
endif()

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_C_STANDARD 11)

if((CMAKE_CXX_COMPILER_ID MATCHES "Clang") OR (CMAKE_CXX_COMPILER_ID MATCHES "GNU"))
    # enforce a clean code
    set(CMAKE_CXX_FLAGS "-Wall -Wextra -Wconversion -Wno-unused-result")
    set(CMAKE_C_FLAGS "-Wall -Wextra -Wconversion -Wno-unused-result")
endif()

if(CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    # clang doesn't have the handy gcc STL header file
    configure_file(stdc++.h.in bits/stdc++.h COPYONLY @ONLY)
    include_directories(${CMAKE_CURRENT_BINARY_DIR})
endif()

enable_testing()


#
# Macros
#

# target to extract the testcases
add_custom_target(extract-testcases
                  COMMAND ${CMAKE_SOURCE_DIR}/runtest.sh -X ${CMAKE_BINARY_DIR}/tests
                  WORKING_DIRECTORY ${CMAKE_BINARY_DIR})

# run a challenge
set(HACKERRANK_CONTEST master)
macro(add_test_hackerrank name)
    add_test(NAME ${name}
             COMMAND ${CMAKE_SOURCE_DIR}/runtest.sh -t ${name} -c ${HACKERRANK_CONTEST} -T ${CMAKE_BINARY_DIR}/tests
             WORKING_DIRECTORY ${CURRENT_BINARY_DIR})
    set_tests_properties(${name} PROPERTIES TIMEOUT 30)
endmacro()

# add a C/C++ challenge
macro(add_hackerrank name src)
    add_executable(${name} ${src})
    add_test_hackerrank(${name})
endmacro(add_hackerrank name src)

# hackerrank problem setters really should improve their code quality
macro(dirty_cpp name)
    target_compile_options("${name}" PRIVATE "-Wno-conversion")
    #target_compile_options("${name}" PRIVATE "-Wno-sign-conversion")
    target_compile_options("${name}" PRIVATE "-Wno-sign-compare")
    target_compile_options("${name}" PRIVATE "-Wno-unused-parameter")
    target_compile_options("${name}" PRIVATE "-Wno-reorder")
    if(CMAKE_CXX_COMPILER_ID MATCHES "Clang")
        target_compile_options("${name}" PRIVATE "-Wno-shorten-64-to-32")
    endif()
endmacro(dirty_cpp name)

# add a Python challenge
macro(add_hackerrank_py name)
    configure_file("${name}" "${name}" COPYONLY @ONLY)
    add_test_hackerrank(${name})
endmacro(add_hackerrank_py name)

# add a Shell challenge
macro(add_hackerrank_shell name)
    configure_file("${name}" "${name}" COPYONLY @ONLY)
    add_test_hackerrank(${name})
endmacro(add_hackerrank_shell name)

# add a Java challenge (only if option is on)
function(add_hackerrank_java src)
    if(HACKERRANK_JAVA)

        cmake_parse_arguments(_hr_java
            ""
            "CLASS"
            ""
            ${ARGN}
        )

        if(NOT DEFINED _hr_java_CLASS)
            set(_hr_java_CLASS Solution)
        endif()

        get_filename_component(name ${src} NAME_WE)
        set(JAR_NAME ${name}_java)
        set(JAVA_SOURCE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/${name}_java)
        file(MAKE_DIRECTORY ${JAVA_SOURCE_DIRECTORY})
        set(JAVA_SOURCE_FILES ${JAVA_SOURCE_DIRECTORY}/${_hr_java_CLASS}.java)
        configure_file(${src} ${JAVA_SOURCE_FILES} COPYONLY @ONLY)

        set(JAVA_DAI_MANIFEST  ${CMAKE_CURRENT_BINARY_DIR}/${name}_java/manifest)
        file(WRITE ${JAVA_DAI_MANIFEST} "Main-Class: ${_hr_java_CLASS}\n")

        add_jar(${JAR_NAME} ${JAVA_SOURCE_FILES} MANIFEST ${JAVA_DAI_MANIFEST}
                OUTPUT_NAME ${name})
        add_test_hackerrank(${name}.jar)
    endif()
endfunction()

# add a Node.js challenge
function(add_hackerrank_js name)
    if(HACKERRANK_JS)
        configure_file("${name}" "${name}" COPYONLY @ONLY)
        add_test_hackerrank(${name})
    endif()
endfunction()



#
# Contests and domains
#

add_subdirectory(mathematics)
add_subdirectory(algorithms)
add_subdirectory(data-structures)
add_subdirectory(cpp)
add_subdirectory(python)
add_subdirectory(shell)
add_subdirectory(c)
add_subdirectory(java)
add_subdirectory(security)
add_subdirectory(regex)
add_subdirectory(tutorials)
add_subdirectory(contests)
add_subdirectory(interview-preparation-kit)

if(HACKERRANK_FP)
    add_subdirectory(fp)
endif()
