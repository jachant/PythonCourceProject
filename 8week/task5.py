"""
https://leetcode.com/problems/fruit-into-baskets/submissions/1467737204/?envType=problem-list-v2&envId=sliding-window
"""

from collections import Counter


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_counter = Counter()
        start_index = 0
        for fruit in fruits:
            fruit_counter[fruit] += 1
            if len(fruit_counter) > 2:
                start_fruit = fruits[start_index]
                fruit_counter[start_fruit] -= 1
                if fruit_counter[start_fruit] == 0:
                    del fruit_counter[start_fruit]
                start_index += 1
        max_length = len(fruits) - start_index
        return max_length
