cmake_minimum_required(VERSION 3.22)
project(futures)

set(CMAKE_CXX_STANDARD 14)

add_executable(futures main.cpp)

target_link_libraries(futures pthread)