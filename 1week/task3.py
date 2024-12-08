"""
https://leetcode.com/problems/count-and-say/submissions/1398472089/?envType=problem-list-v2&envId=string&envType=problem-list-v2&envId=string
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n - 1)
        result = ""
        count = 1
        d = len(prev)
        for i in range(d):
            if i + 1 < d and prev[i] == prev[i + 1]:
                count += 1
            else:
                result += str(count) + prev[i]
                count = 1
        return result
