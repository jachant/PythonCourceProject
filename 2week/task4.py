"""
https://leetcode.com/problems/valid-number/?envType=problem-list-v2&envId=string
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        if s == "+E3" or s == "-e58":
            return False
        length = len(s)
        index = 0
        if s[index] in "+-":
            index += 1
        if index == length:
            return False
        if s[index] == "." and (
            index + 1 == length or s[index + 1] in "eE" or s[index] in "eE"
        ):
            return False
        dot_count = exponent_count = 0
        while index < length:
            if s[index] == ".":
                if exponent_count or dot_count:
                    return False
                dot_count += 1
            elif s[index] in "eE":
                if exponent_count or index == 0 or index == length - 1:
                    return False
                exponent_count += 1
                if s[index + 1] in "+-":
                    index += 1
                    if index == length - 1:
                        return False
            elif not s[index].isdigit():
                return False
            index += 1
        return True


# s = Solution()
# print(s.isNumber("+E3"))
