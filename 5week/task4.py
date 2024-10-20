from collections import defaultdict

"""
https://leetcode.com/problems/clone-graph/submissions/1428780296/?envType=problem-list-v2&envId=hash-table
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        visited = defaultdict(Node)

        def clone(node: "Node") -> "Node":
            if node is None:
                return None
            if node in visited:
                return visited[node]
            clone_node = Node(node.val)
            visited[node] = clone_node
            for neighbor in node.neighbors:
                clone_node.neighbors.append(clone(neighbor))
            return clone_node

        return clone(node)
