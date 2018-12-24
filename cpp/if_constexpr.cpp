// https://linuxfr.org/news/cpp17-branche-a-la-compilation-if-constexpr
// https://tech.io/playgrounds/2205/7-features-of-c17-that-will-simplify-your-code/constexpr-if
//  g++ -Wall -Werror -Wextra -ansi -pedantic -std=c++17 -o if_constexpr if_constexpr.cpp

#include <iostream>
#include <memory>

template <typename T>
auto get_value(T t) {
    if constexpr (std::is_pointer_v<T>)
        return *t;
    else
        return t;
}

int main()
{
     auto pi = std::make_unique<int>(9);
     int i = 9;
     
     std::cout << get_value(pi.get()) << "\n";
     std::cout << get_value(i) << "\n";
}
