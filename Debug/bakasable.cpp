
#include <execinfo.h>
#include <iostream>
using namespace std;

static void show_backtrace (void) {
    void *buffer[100];
    char **strings;
    int nptrs, j;
    nptrs = backtrace(buffer, 100);
    printf("backtrace() returned %d addresses\n", nptrs);

    /* The call backtrace_symbols_fd(buffer, nptrs, STDOUT_FILENO)
    would produce similar output to the following: */

    strings = backtrace_symbols(buffer, nptrs);
    if (strings == NULL) {
        printf("backtrace_symbols ERROR !\n");
    } else {
        for (j = 0; j < nptrs; j++)
            printf("%s\n", strings[j]);
        free(strings);
    }
}

void foobar(int i)
{
    cout << "Foobar Start!\n";
    if ( i == 3 )
        show_backtrace();
    cout << "Foobar End!\n";
}

int main (int argc, char **argv)
{
    cout << "Does it work?\n";
    if (argc == 2)
        foobar(atoi(argv[1]));
    cout << "End!\n";
    return 0;
}
