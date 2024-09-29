"""
https://leetcode.com/problems/determine-if-two-strings-are-close/
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if (
            (not (len(word1) == len(word2)))
            or (not (set(word1) == set(word2)))
            or (not (self.check(word1) == self.check(word2)))
        ):
            return False
        return True

    def check(self, s: str):
        ans = dict()
        for i in s:
            if i not in ans:
                ans[i] = 0
            ans[i] += 1
        return sorted(ans.values())
