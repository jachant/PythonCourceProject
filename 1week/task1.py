"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=string
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen, start = 0, 0
        length = dict()
        l = len(s)
        for i in range(l):
            if s[i] in length:
                start = max(start, length[s[i]] + 1)
                length[s[i]] = i
                maxLen = max(maxLen, i - start + 1)
                # print(start)
                # print(maxLen)
            else:
                length[s[i]] = i
                maxLen = max(maxLen, i - start + 1)
                # print(maxLen)
        return maxLen
