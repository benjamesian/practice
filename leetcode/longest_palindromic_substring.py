#!/usr/bin/python3


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        l = len(s)
        for ix in range(l):
            if 2 * (l - ix) < len(longest):
                break
            i = j = 0

            while ix >= i and ix + i < l and s[ix - i] == s[ix + i]:
                i += 1

            while ix >= j and ix + 1 + j < l and s[ix - j] == s[ix + 1 + j]:
                j += 1

            if len(longest) < 2 * i - 1 >= 2 * j:
                longest = s[ix - i + 1: ix + i]
                ix += i
            elif len(longest) < 2 * j:
                longest = s[ix - j + 1: ix + 1 + j]
                ix += j

        return longest
