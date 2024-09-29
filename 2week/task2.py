"""
https://leetcode.com/problems/integer-to-roman/?envType=problem-list-v2&envId=string
"""


class Solution:
    def intToRoman(self, num: int) -> str:

        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        symbol_value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = str()
        for i, value in enumerate(symbol):
            while num >= symbol_value[i]:
                res += value

                num -= symbol_value[i]

        return res


# s = Solution()
# print(s.intToRoman(3456))
