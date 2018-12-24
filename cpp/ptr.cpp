// 'Hello World!' program 
// g++ -Wall -Werror -Wextra -ansi -pedantic -std=c++17 -o ptr ptr.cpp

#include <iostream>
#include <memory>

class tuple
{
public:
    tuple() : key("Hello"), value("World!") {};
    std::string c_str() const { return key + ": " + value; }
private:
    std::string key;
    std::string value;
};

int main()
{
    // Standard
    {
        tuple t = tuple();
        std::cout << t.c_str() << std::endl;
    }
    
    // 
    {
        tuple *t = new tuple();
        std::cout << t->c_str() << std::endl;
    }
    
    // https://fr.cppreference.com/w/cpp/memory/unique_ptr
    {
        std::unique_ptr<tuple> t(new tuple);
        std::cout << t->c_str() << std::endl;
    }
    return 0;
}

