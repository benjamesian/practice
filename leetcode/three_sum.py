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
            for e in nums[i+1:]:
                if e in seen:
                    continue
                if e > target - e:
                    break
                if e == target - e and ht[e] < 2:
                    break
                if ht.get(target - e):
                    solutions.append([-target, e, target - e])
                    seen.add(e)

        while i < len(nums) - 2:
            n = nums[i]
            ht[n] -= 1
            twoSum(-n)
            i += ht[n] + 1
            del ht[n]

        return solutions
