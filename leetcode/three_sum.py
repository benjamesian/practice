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
                e3 = -(e1 + e2)
                # break conditions first for speed
                if e2 > e3:
                    # if possible would've been added earlier, will be true for further iterations
                    break
                if e2 == e3 and ht[e2] == 1:
                    # e2 and e3 are not distinct in nums, would catch on previous break next iter so break now
                    break
                if e2 in seen or not ht.get(e3):
                    # will not produce a new solution
                    continue
                solutions.append([e1, e2, e3])
                seen.add(e2)
                seen.add(e3)

        while i < len(nums) - 2:
            n = nums[i]
            ht[n] -= 1
            twoSum(-n)
            # no longer need to consider `n`
            i += ht[n] + 1
            del ht[n]

        return solutions
