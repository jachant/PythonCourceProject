"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/?envType=problem-list-v2&envId=binary-tree
"""


class Solution:

    def give_root(self, root):
        if not root or (not root.left and not root.right):
            return root

        newLeft = self.give_root(root.left)
        newRight = self.give_root(root.right)

        curr = newLeft
        if not curr:
            return root

        while curr.right:
            curr = curr.right

        curr.right = newRight
        root.left = None
        root.right = newLeft

        return root

    def flatten(self, root: Optional[TreeNode]) -> None:
        root = self.give_root(root)
