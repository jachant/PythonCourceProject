"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/submissions/1480122640/?envType=problem-list-v2&envId=binary-tree
"""


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = deque()

        if not root:
            return []
        queue.append(root)

        def dfs(ans, queue):
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if queue:
                dfs(ans, queue)
            ans.append(temp)

        dfs(ans, queue)
        return ans
