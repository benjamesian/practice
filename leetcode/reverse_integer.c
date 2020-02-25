#include <limits.h>

//https://leetcode.com/problems/reverse-integer/
int reverse(int x)
{
    int y = x, pw = 1, neg = 0;
    if (x == INT_MIN)
        return (0);
    if (x < 0)
    {
        neg = 1;
        x = -x;
    }
    if (x < 10)
        return (x);
    while (y /= 10)
        pw *= 10;
    y = 0;
    while (x)
    {
        if ((INT_MAX - y) / pw < x % 10)
            return (0);
        y += pw * (x % 10);
        pw /= 10;
        x /= 10;
    }

    return (neg ? -y : y);
}