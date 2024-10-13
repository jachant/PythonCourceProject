"""
https://leetcode.com/problems/combination-sum/submissions/1420870365/?envType=problem-list-v2&envId=array
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(index: int, current_sum: int):
            if current_sum == 0:
                combinations.append(combination_so_far[:])
                return
            if index >= len(candidates) or current_sum < candidates[index]:
                return
            dfs(index + 1, current_sum)
            combination_so_far.append(candidates[index])
            dfs(index, current_sum - candidates[index])
            combination_so_far.pop()

        candidates.sort()
        combination_so_far = []
        combinations = []
        dfs(0, target)
        return combinations
