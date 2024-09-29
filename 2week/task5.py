"""
https://leetcode.com/problems/simplify-path/?envType=problem-list-v2&envId=string
"""


class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        for part in path.split("/"):

            if not part or part == ".":
                continue

            elif part == "..":
                if stack:
                    stack.pop()

            else:
                stack.append(part)
        simplified_path = "/" + "/".join(stack)
        return simplified_path
