"""
https://leetcode.com/problems/get-equal-substrings-within-budget/submissions/1455193973/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def equalSubstring(self, s: str, t: str, max_cost: int) -> int:
        n = len(s)
        total_cost = 0
        start_index = 0
        max_length = 0
        for end_index in range(n):
            total_cost += abs(ord(s[end_index]) - ord(t[end_index]))
            while total_cost > max_cost:
                total_cost -= abs(ord(s[start_index]) - ord(t[start_index]))
                start_index += 1
            max_length = max(max_length, end_index - start_index + 1)
        return max_length
