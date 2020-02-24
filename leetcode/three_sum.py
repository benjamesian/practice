#!/usr/bin/python3
from collections import Counter


# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ht = Counter(nums)
        solutions = []
        n = 0
        s = set()

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            for e in nums:
                if 2 * e > target or (e * 2 == target and ht[e] < 2):
                    break
                if e in s:
                    continue
                if ht.get(target - e):
                    solutions.append([n, e, target - e])
                    s.add(e)
            s.clear()

        i = 0
        while i < len(nums) - 2:
            n = nums[i]
            ht[n] -= 1
            twoSum(nums[i+1:], -nums[i])
            i += ht[n] + 1
            del ht[n]

        return solutions
