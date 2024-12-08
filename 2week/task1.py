"""
https://leetcode.com/problems/longest-palindromic-substring/?envType=problem-list-v2&envId=string
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if self.check(s):
            return s
        ans = ""
        k = len(s)
        for i in range(0, k):
            for j in range(i + 1, k + 1):

                newStr = s[i:j]

                if len(ans) < len(newStr) and self.check(newStr):
                    ans = newStr
        return ans

    def check(self, s: str):
        s1 = s[::-1]
        return s == s1


s = Solution()
print(s.longestPalindrome("abb"))
