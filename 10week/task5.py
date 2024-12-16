"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/?envType=problem-list-v2&envId=binary-tree
"""

from collections import deque


class Solution:
    def connect(self, root: "Node") -> "Node":
        if root == None:
            return None
        q = deque([root])
        while q:  # [1] [3,4,5]
            size = len(q)  # 1 2
            while size > 0:  #  > 0
                node = q.popleft()  # node =1,2,3
                if size > 1:  #
                    node.next = q[0]  #  2.next = 3
                size -= 1  # size =1

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
