from bisect import bisect_left

"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/1420863131/?envType=problem-list-v2&envId=array
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_index = bisect_left(nums, target)
        right_index = bisect_left(nums, target + 1)
        if left_index == right_index:
            return [-1, -1]
        else:
            return [left_index, right_index - 1]
