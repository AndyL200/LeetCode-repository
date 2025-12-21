#include <iostream>
int fib(int n) {
    if(n <= 0)
    {
        return 0;
    }
    else if(n == 1)
    {
        return 1;
    }

    int p0 = 0;
    int p1 = 1;
    int p2 = 1;
    n -= 1;

    while(n > 0)
    {
        p2 = p1 + p0;
        p0 = p1;
        p1 = p2;
        n--;
    }
    return p2;
}