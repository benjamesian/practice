#!/usr/bin/python3
from collections import Counter


# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ht = Counter(nums)
        solutions = []
        n = i = 0

        def twoSum(target: int) -> List[List[int]]:
            seen = set()
            e1 = -target
            for e2 in nums[i+1:]:
                if e2 in seen:
                    continue
                e3 = -(e1 + e2)
                if e2 > e3:
                    break
                if e2 == e3 and ht[e2] == 1:
                    break
                if ht.get(e3):
                    solutions.append([e1, e2, e3])
                    seen.add(e2)
                    seen.add(e3)

        while i < len(nums) - 2:
            n = nums[i]
            ht[n] -= 1
            twoSum(-n)
            i += ht[n] + 1
            del ht[n]

        return solutions
