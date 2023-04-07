cmake_minimum_required(VERSION 3.22)
project(threads)

set(CMAKE_CXX_STANDARD 14)

add_executable(threads main.cpp)

target_link_libraries(threads pthread)

