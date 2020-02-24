#include <limits.h>

//https://leetcode.com/problems/string-to-integer-atoi/
int myAtoi(char *str)
{
    int negative = 0, out = 0;

    while (*str == ' ')
        str++;
    if (*str == '-')
        negative = 1;
    if (*str == '+' || *str == '-')
        str++;
    if (*str < '0' || '9' < *str)
        return (0);
    while ('0' <= *str && *str <= '9')
    {
        if ((INT_MAX - (*str - '0')) / 10 < out)
            return (negative ? INT_MIN : INT_MAX);
        out = 10 * out + (*str - '0');
        str++;
    }

    return (negative ? -out : out);
}