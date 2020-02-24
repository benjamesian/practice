#!/usr/bin/python3
from sys import argv


def longest_palindrome(s):
    longest = ''
    l = len(s)
    for ix in range(l):
        i = j = 0

        while ix - i >= 0 and ix + i < l and s[ix - i] == s[ix + i]:
            i += 1
        while ix - j >= 0 and ix + 1 + j < l and s[ix - j] == s[ix + 1 + j]:
            j += 1

        if 2 * i - 1 >= 2 * j:
            cur = s[ix - i + 1 : ix + i]
        else:
            cur = s[ix - j + 1 : ix + 1 + j]

        if len(cur) > len(longest):
            longest = cur

    return longest


if __name__ == '__main__':
    print(longest_palindrome(argv[1]))
    print(longest_palindrome('banana'))
    print(longest_palindrome('bananarama'))
    print(longest_palindrome('abc'))
    print(longest_palindrome('million'))
