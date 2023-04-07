// g++ -Wall -Werror -Wextra -ansi -pedantic -std=c++17 -o vector main.cpp && ./vector

#include <algorithm>
#include <iostream>
#include <vector>

//===========================

template <typename T>
void Shows( std::vector<T>& Vec ) {
    std::cout << "Show elements : ";
    for (T& i: Vec) // C++11
        std::cout << i << ' ';
    std::cout << std::endl;
}

template <typename T>
void Shows_reverse( std::vector<T>& Vec ) {
    std::cout << "Show elements in reverse : ";
    for (std::vector<int>::const_reverse_iterator rit = Vec.crbegin() ; rit != Vec.crend() ; ++rit)
        std::cout << *rit << ' ';
    std::cout << std::endl;
}

//===========================
// https://www.cplusplus.com/reference/algorithm/find/

template <typename T>
bool Contains( std::vector<T>& Vec, const T& Element )
{
    if (std::find(Vec.begin(), Vec.end(), Element) != Vec.end())
    {
        std::cout << "Search element " << Element << ": Found in " << Vec.size() << " elements" << std::endl;
        return true;
    }

    std::cout << "Search element " << Element << ": NOT Found in " << Vec.size() << " elements" << std::endl;
    return false;
}

//===========================
// http://www.cplusplus.com/reference/vector/vector/erase/
// https://www.cplusplus.com/reference/algorithm/remove/

template <typename T>
void Remove_element( std::vector<T>& Vec, const T& Element )
{
    std::cout << "Try to remove element " << Element << " in " << Vec.size() << " elements" << std::endl;
    Vec.erase(std::remove(Vec.begin(), Vec.end(), Element), Vec.end());
}

//===========================
// https://www.cplusplus.com/reference/algorithm/remove_if/
// https://en.cppreference.com/w/cpp/algorithm/remove

template <typename T>
void Remove_element_lower_than( std::vector<T>& Vec, const T& Element )
{
    std::cout << "Try to remove elements lower than " << Element << " in " << Vec.size() << " elements" << std::endl;
    Vec.erase(
        std::remove_if(
                Vec.begin(),
                Vec.end(),
                [&](const T& x) {return x < Element;}), // equals to : [Element](const T& x) -> bool {return x < Element;}),
        Vec.end());
}

//===========================

void Remove_even_numbers_with_iterator( std::vector<int>& Vec ) {
    std::cout << "Erase all even numbers (C++11 and later)" << std::endl;
    for (std::vector<int>::iterator it = Vec.begin(); it != Vec.end();) {
        if (*it % 2 == 0) {
            it = Vec.erase(it);
        } else {
            ++it;
        }
    }
}

//===========================

int main()
{
    std::vector<int> myvec { 7, 8, 9, 10, 11 };

    std::vector<int>::iterator it = myvec.begin();
    printf("First element : %d\n", *it);
    it = myvec.end() - 1;
    printf("Last element : %d\n", *it);

    // Show elements : 7 8 9 10 11
    Shows(myvec);

    // Show elements in reverse : 11 10 9 8 7
    Shows_reverse(myvec);

    // Search element 8: Found in 5 elements
    Contains(myvec, 8);

    // Try to remove element 8 in 5 elements
    Remove_element(myvec, 8);

    // Show elements : 7 9 10 11
    Shows(myvec);

    // Search element 8: NOT Found in 4 elements
    Contains(myvec, 8);

    // Try to remove elements lower than 10 in 4 elements
    Remove_element_lower_than(myvec, 10);

    // Show elements : 10 11
    Shows(myvec);

    // Search element 10: Found in 2 elements
    Contains(myvec, 10);

    // Erase all even numbers (C++11 and later)
    Remove_even_numbers_with_iterator(myvec);

    // Show elements : 11
    Shows(myvec);

    return 0;
}

//===========================
