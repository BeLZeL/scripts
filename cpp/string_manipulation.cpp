// g++ -Wall -Werror -Wextra -ansi -pedantic -std=c++17 -o string_manipulation string_manipulation.cpp && ./string_manipulation
/*
AYZe;Wh< is encrypted to B[]i@]oD
AYZe;Wh< =? AYZe;Wh<
*/

#include <string>
#include <stdio.h>
#include <stddef.h>

std::string encrypt(const std::string& in)
{
    std::string sb;

    for (size_t i = 0; i < in.length(); i++)
    {
        int code = in.at(i);
        code += i + 1;
        while (code > 127) {
            code = code - 127 + 31;
        }
        char c = (char) code;
        sb.push_back(c);
    }
    return sb;
}

std::string decrypt(const std::string & in)
{
    std::string sb;

    for (size_t i = 0; i < in.length(); i++)
    {
        int code = in.at(i);
        if (code < 32 || code > 127) {
            sb.push_back((char)code);
            continue;
        }

        code -= (i + 1);
        while (code < 32) {
            code = code + 127 - 31;
        }
        char c = (char) code;
        sb.push_back(c);
    }
    return sb;
}

//===========================

int main()
{   
    std::string str("AYZe;Wh<");

    printf("%s is encrypted to %s\n", str.c_str(), encrypt(str).c_str());
    printf("%s =? %s\n", str.c_str(), decrypt(encrypt(str)).c_str());        

    return 0;
}

//===========================
