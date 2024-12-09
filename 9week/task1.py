"""
https://leetcode.com/problems/unique-binary-search-trees/?envType=problem-list-v2&envId=binary-tree
"""


class Solution:
    def numTrees(self, n: int) -> int:
        num_trees = [0] * (n + 1)
        num_trees[0] = 1
        for nodes in range(1, n + 1):
            for left_tree_nodes in range(nodes):
                num_trees[nodes] += (
                    num_trees[left_tree_nodes] * num_trees[nodes - left_tree_nodes - 1]
                )
        return num_trees[-1]
