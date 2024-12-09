"""
https://leetcode.com/problems/validate-binary-search-tree/?envType=problem-list-v2&envId=binary-tree
"""


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True
            if (min_val is not None and node.val <= min_val) or (
                max_val is not None and node.val >= max_val
            ):
                return False
            return validate(node.left, min_val, node.val) and validate(
                node.right, node.val, max_val
            )

        return validate(root, None, None)
