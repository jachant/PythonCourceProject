"""
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/submissions/1467733256/?envType=problem-list-v2&envId=sliding-window
"""

from collections import Counter
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        flat_list = [
            (value, idx) for idx, sublist in enumerate(nums) for value in sublist
        ]
        flat_list.sort()
        count = Counter()
        result = [float("-inf"), float("inf")]
        pointer = 0
        for right_value, origin_list_index in flat_list:
            count[origin_list_index] += 1
            while len(count) == len(nums):
                left_value = flat_list[pointer][0]
                size_difference = right_value - left_value - (result[1] - result[0])
                if size_difference < 0 or (
                    size_difference == 0 and left_value < result[0]
                ):
                    result = [left_value, right_value]
                left_origin_index = flat_list[pointer][1]
                count[left_origin_index] -= 1
                if count[left_origin_index] == 0:
                    count.pop(left_origin_index)
                pointer += 1
        return result
