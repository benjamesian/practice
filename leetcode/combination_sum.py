#!/usr/bin/python3
# https://leetcode.com/problems/combination-sum/


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = list(set(candidates))
        candidates.sort()
        return self.helper(candidates, target)

    def helper(self, candidates: List[int], target: int) -> List[List[int]]:
        sols = []

        if not (candidates and 0 < candidates[0] <= target):
            return sols

        if candidates[0] == target:
            return [[candidates[0]]]

        sols += [[candidates[0], *comb] for comb in
                 self.helper(candidates, target - candidates[0])]

        return sols + self.helper(candidates[1:], target)
