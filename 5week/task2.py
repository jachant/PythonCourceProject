from collections import Counter
from math import inf

"""
https://leetcode.com/problems/minimum-window-substring/submissions/1428776693/?envType=problem-list-v2&envId=hash-table
"""


class Solution:
    def minWindow(self, source: str, target: str) -> str:
        target_counter = Counter(target)
        window_counter = Counter()
        valid_char_count = 0
        left = 0
        min_left = -1
        min_size = inf
        for right, char in enumerate(source):
            window_counter[char] += 1
            if target_counter[char] >= window_counter[char]:
                valid_char_count += 1
            while valid_char_count == len(target):
                if right - left + 1 < min_size:
                    min_size = right - left + 1
                    min_left = left
                if target_counter[source[left]] >= window_counter[source[left]]:
                    valid_char_count -= 1
                window_counter[source[left]] -= 1
                left += 1
        return "" if min_left < 0 else source[min_left : min_left + min_size]
