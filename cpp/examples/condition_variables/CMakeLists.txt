cmake_minimum_required(VERSION 3.22)
project(condition_variables)

set(CMAKE_CXX_STANDARD 14)

add_executable(condition_variables main.cpp)

target_link_libraries(condition_variables pthread)