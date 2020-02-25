#!/usr/bin/python3
# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        arr.reverse()
        return ' '.join(arr)
