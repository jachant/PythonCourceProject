"""
https://leetcode.com/problems/jump-game-ii/submissions/1420874114/?envType=problem-list-v2&envId=array
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_count = max_reach = last_reach = 0
        for index, value in enumerate(nums[:-1]):
            max_reach = max(max_reach, index + value)
            if last_reach == index:
                jump_count += 1
                last_reach = max_reach
        return jump_count
