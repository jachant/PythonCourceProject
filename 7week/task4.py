"""
https://leetcode.com/problems/sliding-window-maximum/?envType=problem-list-v2&envId=sliding-window
"""

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        index_queue = deque()
        max_values = []
        for current_index, value in enumerate(nums):
            if index_queue and current_index - k + 1 > index_queue[0]:
                index_queue.popleft()
            while index_queue and nums[index_queue[-1]] <= value:
                index_queue.pop()
            index_queue.append(current_index)
            if current_index >= k - 1:
                max_values.append(nums[index_queue[0]])
        return max_values
