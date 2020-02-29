# https://leetcode.com/problems/buddy-strings/
from collections import Counter


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or len(A) < 2:
            return False

        swappers = []
        for (a, b) in zip(A, B):
            if a != b:
                swappers.append((a, b))

        if len(swappers) == 0:
            if max(Counter(A).values()) > 1:
                return True
        if len(swappers) != 2:
            return False
        if swappers[0][0] == swappers[1][1] and swappers[0][1] == swappers[1][0]:
            return True

        return False
