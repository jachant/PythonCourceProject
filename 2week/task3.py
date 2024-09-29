"""
https://leetcode.com/problems/generate-parentheses/?envType=problem-list-v2&envId=string
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack("", 0, 0, n, res)
        return res

    def backtrack(self, s, left, right, n, res):
        if len(s) == 2 * n:
            res.append(s)
            return
        if left < n:
            self.backtrack(s + "(", left + 1, right, n, res)
        if right < left:
            self.backtrack(s + ")", left, right + 1, n, res)


# s = Solution()
# print(s.generateParenthesis(3))
