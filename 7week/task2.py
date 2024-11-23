"""
https://leetcode.com/problems/minimum-size-subarray-sum/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length_of_nums = len(nums)
        min_length = length_of_nums + 1
        sum_of_subarray = start_index = 0
        for end_index, value in enumerate(nums):
            sum_of_subarray += value
            while start_index < length_of_nums and sum_of_subarray >= target:
                min_length = min(min_length, end_index - start_index + 1)
                sum_of_subarray -= nums[start_index]
                start_index += 1
        return min_length if min_length <= length_of_nums else 0
