// g++ -Wall -Werror -Wextra -ansi -pedantic -std=c++17 -o unique_ptr unique_ptr.cpp && ./unique_ptr
// https://fr.cppreference.com/w/cpp/memory/unique_ptr
/*
Foo::Foo
Foo::bar
f(const Foo&)
Foo::bar
destruction de p2...
Foo::bar
Foo::~Foo
 */
#include <iostream>
#include <vector>
#include <memory>

//===========================

struct Foo {
    Foo() { std::cout << "Foo::Foo\n"; }
    ~Foo() { std::cout << "Foo::~Foo\n"; }
    void bar() const { std::cout << "Foo::bar\n"; }
};
 
void f(const Foo &foo)
{
    std::cout << "f(const Foo&)\n";
    foo.bar();
}

//===========================

void swap_unique_ptr()
{
    std::cout << "\\/----------------------\\/\n";
    std::unique_ptr<Foo> p1(new Foo);  // p1 possède Foo
    if (p1) p1->bar();
 
    {
        std::unique_ptr<Foo> p2(std::move(p1));  // maintenant p2 possède Foo
        f(*p2);
 
        p1 = std::move(p2);  // la propriété retourne à p1
        std::cout << "destruction de p2...\n";
    }
 
    if (p1) p1->bar();
 
    // L'instance de Foo est détruite lorsque p1 devient inaccessible
    std::cout << "/\\----------------------/\\\n";
}

//===========================

void vector_unique_ptr()
{
    std::cout << "\\/----------------------\\/\n";
    std::unique_ptr<Foo> p(new Foo);
    std::vector<std::unique_ptr<Foo>> vec;
    vec.push_back(std::move(p));
    for ( std::unique_ptr<Foo> &i : vec )
        i->bar();
    std::cout << "/\\----------------------/\\\n";
}

//===========================

int main()
{    
    swap_unique_ptr();
    vector_unique_ptr();
}

//===========================
