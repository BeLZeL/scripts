// g++ -Wall -Werror -Wextra -ansi -pedantic -std=c++17 -o const_ptr const_ptr.cpp && ./const_ptr
// const pointers
// ptr[1] <==> *(ptr + 1)

#include <iostream>

/******************************************************************************
#!/usr/bin/env python3
# Generate const_ptr.cpp

# Transform string to char
def t(str):    
        return 'c' if str.startswith('const') else '.'

list_char    = ['', 'const']
list_pointer = ['', 'const']
cpt = 0

# With return
list_code    = [ 'return ptr;' ]
list_return  = ['char *', 'const char *']
prototype    = '{0:>12s} func_{1:02d} ( {2:5s} char * {3:5s} ptr )'

for code in list_code:
    for ret in list_return:
        for ch in list_char:
            for ptr in list_pointer:
                cpt+=1
                
                line = prototype.format(ret, cpt, ch, ptr) + " { " + code + " }"
                if not ret.startswith('const') and ch.startswith('const'):
                    print("//" + line + " // error: invalid conversion from ‘const char*’ to ‘char*’ [-fpermissive]")
                else:
                    print("  " + line)
                
print('')

# Without return
list_code    = [ "ptr[0] = '{0}'; ptr[1] = '{1}'; ptr[2] = '{2}';",
                 'ptr++;'
               ]
list_return  = ['void']
prototype    = '{0} func_{1:02d} ( {2:5s} char * {3:5s} ptr )'

for code in list_code:
    for ret in list_return:
        for ch in list_char:
            for ptr in list_pointer:
                cpt+=1
                
                line = prototype.format(ret, cpt, ch, ptr) + " { " + code.format(t(ret), t(ch), t(ptr)) + " }" 
                if ptr.startswith('const') and code == 'ptr++;':
                    print("//" + line + " // error: increment of read-only parameter ‘ptr’")
                elif ch.startswith('const') and code.startswith('ptr[0]') and ptr.startswith('const'):
                    print("//" + line + " // error: assignment of read-only location ‘*(const char*)ptr’")
                elif ch.startswith('const') and code.startswith('ptr[0]') and not ptr:
                    print("//" + line + " // error: assignment of read-only location ‘* ptr’")
                else:
                    print("  " + line)
******************************************************************************/
///////////////////////////////////////////////////////////////////////////////
        char * func_01 (       char *       ptr ) { return ptr; }
        char * func_02 (       char * const ptr ) { return ptr; }
//      char * func_03 ( const char *       ptr ) { return ptr; } // error: invalid conversion from ‘const char*’ to ‘char*’ [-fpermissive]
//      char * func_04 ( const char * const ptr ) { return ptr; } // error: invalid conversion from ‘const char*’ to ‘char*’ [-fpermissive]
  const char * func_05 (       char *       ptr ) { return ptr; }
  const char * func_06 (       char * const ptr ) { return ptr; }
  const char * func_07 ( const char *       ptr ) { return ptr; }
  const char * func_08 ( const char * const ptr ) { return ptr; }

  void func_09 (       char *       ptr ) { ptr[0] = '.'; ptr[1] = '.'; ptr[2] = '.'; }
  void func_10 (       char * const ptr ) { ptr[0] = '.'; ptr[1] = '.'; ptr[2] = 'c'; }
//void func_11 ( const char *       ptr ) { ptr[0] = '.'; ptr[1] = 'c'; ptr[2] = '.'; } // error: assignment of read-only location ‘* ptr’
//void func_12 ( const char * const ptr ) { ptr[0] = '.'; ptr[1] = 'c'; ptr[2] = 'c'; } // error: assignment of read-only location ‘*(const char*)ptr’
  void func_13 (       char *       ptr ) { ptr++; }
//void func_14 (       char * const ptr ) { ptr++; } // error: increment of read-only parameter ‘ptr’
  void func_15 ( const char *       ptr ) { ptr++; }
//void func_16 ( const char * const ptr ) { ptr++; } // error: increment of read-only parameter ‘ptr’
///////////////////////////////////////////////////////////////////////////////

int main()
{
    char *ptr = new char[4];

    std::cout << "Before : " << ptr << std::endl; func_09(ptr); std::cout << "After  : " << ptr << std::endl;
    std::cout << "Before : " << ptr << std::endl; func_10(ptr); std::cout << "After  : " << ptr << std::endl;
    
    std::cout << "Before : " << ptr << std::endl; std::cout << "After  : " << func_23(ptr) << " (" << ptr << ")" << std::endl;
    
    free(ptr);
    
    return 0;
}

