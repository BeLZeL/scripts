// g++ -Wall -Werror -Wextra -ansi -pedantic -std=c++17 -o vector vector.cpp && ./vector
/*
2: Found with size 4
2: NOT Found with size 3
4: Found with size 1
*/

#include <algorithm>
#include <iostream>
#include <vector>

//===========================

template <typename T> 
bool Contains( std::vector<T>& Vec, const T& Element )
{
    if (std::find(Vec.begin(), Vec.end(), Element) != Vec.end())
    {
        std::cout << Element << ": Found with size " << Vec.size() << std::endl;
        return true;
    }

    std::cout << Element << ": NOT Found with size " << Vec.size() << std::endl;
    return false;
}

//===========================
// http://www.cplusplus.com/reference/vector/vector/erase/

template <typename T>
void Remove_element( std::vector<T>& Vec, const T& Element )
{
    Vec.erase(std::remove(Vec.begin(), Vec.end(), Element), Vec.end());
}

//===========================
// https://en.cppreference.com/w/cpp/algorithm/remove

template <typename T> 
void Remove_element_lower_than( std::vector<T>& Vec, const T& Element )
{
    Vec.erase(std::remove_if(Vec.begin(), Vec.end(), [Element](const T& x) -> bool {return x < Element;}), Vec.end());
}

//===========================

int main()
{   
    std::vector<int> myvec = { 1, 2, 3, 4 };

    Contains(myvec, 2);
    
    Remove_element(myvec, 2);
    
    Contains(myvec, 2);
    
    Remove_element_lower_than(myvec, 4);
    
    Contains(myvec, 4);
    
    return 0;
}

//===========================
