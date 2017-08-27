#include <bakasable.hpp>

#include <iostream>

struct A { double x; };
const A* a = new A{0};

decltype(a->x) y;       // type of y is double (declared type)
decltype((a->x)) z = y; // type of z is const double& (lvalue expression)

template<typename T, typename U>
auto add(T t, U u) -> decltype(t + u); // return type depends on template parameters

int main()
{
    int i = 33;
    decltype(i) j = i * 2.3;
    double  k = i * 2.3;

    std::cout << "i = " << i << ", "  // 33
              << "j = " << j << ", "  // 75
              << "k = " << k << '\n'; // 75.9

    auto f = [](int a, int b) -> int
    {
        return a * b;
    };

    decltype(f) g = f; // the type of a lambda function is unique and unnamed
    i = f(2, 2);
    j = g(3, 3);

    std::cout << "i = " << i << ", "  // 4
              << "j = " << j << "\n";  // 9
}
