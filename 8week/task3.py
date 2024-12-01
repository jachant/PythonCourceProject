"""
https://leetcode.com/problems/subarray-product-less-than-k/description/?envType=problem-list-v2&envId=sliding-window
"""

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count_subarrays = 0
        product = 1
        start_index = 0
        for end_index, value in enumerate(nums):
            product *= value
            while start_index <= end_index and product >= k:
                product //= nums[start_index]
                start_index += 1
            count_subarrays += end_index - start_index + 1
        return count_subarrays
