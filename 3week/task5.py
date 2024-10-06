"""
https://leetcode.com/problems/next-permutation/submissions/1413894998/?envType=problem-list-v2&envId=array
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i == 0:
            nums.reverse()
            return

        j = len(nums) - 1
        while nums[j] <= nums[i - 1]:
            j -= 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        nums[i:] = nums[i:][::-1]
