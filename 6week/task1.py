"""
https://leetcode.com/problems/longest-duplicate-substring/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def has_duplicate(length):
            seen = set()
            for i in range(n - length + 1):
                substring = s[i : i + length]
                if substring in seen:
                    return substring
                seen.add(substring)
            return ""

        n = len(s)
        left, right = 0, n
        longest_dup = ""
        while left < right:
            mid = (left + right + 1) // 2
            current_dup = has_duplicate(mid)
            longest_dup = current_dup or longest_dup
            if current_dup:
                left = mid
            else:
                right = mid - 1
        return longest_dup
