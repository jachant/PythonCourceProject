"""
https://leetcode.com/problems/longest-consecutive-sequence/submissions/1428779491/?envType=problem-list-v2&envId=hash-table
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0
        for number in nums:
            if number - 1 not in num_set:
                current_num = number
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak
