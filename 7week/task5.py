"""
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/?envType=problem-list-v2&envId=sliding-window
"""

from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dfs(left, right):
            counter = Counter(s[left : right + 1])
            split_char = next(
                (char for char, freq in counter.items() if freq < k), None
            )
            if not split_char:
                return right - left + 1

            max_length = 0
            i = left
            while i <= right:
                while i <= right and s[i] == split_char:
                    i += 1
                if i > right:
                    break
                j = i
                while j <= right and s[j] != split_char:
                    j += 1
                current_length = dfs(i, j - 1)
                max_length = max(max_length, current_length)
                i = j
            return max_length

        return dfs(0, len(s) - 1)
