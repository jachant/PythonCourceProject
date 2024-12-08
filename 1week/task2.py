"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=problem-list-v2&envId=string&envType=problem-list-v2&envId=string
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combines = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        ans = []
        if digits:
            for i in combines[digits[0]]:
                ans.append(i)
            for number in digits[1:]:
                for _ in range(len(ans)):
                    f = ans.pop(0)
                    for i in combines[number]:
                        ans.append(f + i)
        return ans
