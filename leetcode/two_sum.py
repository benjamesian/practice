#!/usr/bin/python3
# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ns = {}
        for k, v in enumerate(nums):
            if target - v in ns:
                return [ns[target - v], k]
            ns[v] = k
