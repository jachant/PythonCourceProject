"""
https://leetcode.com/problems/contains-duplicate-iii/submissions/1461098634/?envType=problem-list-v2&envId=sliding-window
"""

from typing import List

from sortedcontainers import SortedSet


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], index_diff: int, value_diff: int
    ) -> bool:
        sorted_set = SortedSet()
        for i, num in enumerate(nums):
            left_boundary_index = sorted_set.bisect_left(num - value_diff)
            if (
                left_boundary_index < len(sorted_set)
                and sorted_set[left_boundary_index] <= num + value_diff
            ):
                return True
            sorted_set.add(num)
            if i >= index_diff:
                sorted_set.remove(nums[i - index_diff])
        return False
