"""
https://leetcode.com/problems/group-anagrams/?envType=problem-list-v2&envId=string&envType=problem-list-v2&envId=string
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = dict()
        for s in strs:
            sorted_s = "".join(sorted(s))
            # print(sorted_s)
            if sorted_s in hashMap:
                hashMap[sorted_s].append(s)
            else:
                hashMap[sorted_s] = [s]
        # print(hashMap.values())
        return list(hashMap.values())
