"""
Question:
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            pi = lo + (hi - lo) // 2 # this is our pivot
            if nums[pi] == target:
                return pi
            elif target < nums[pi]:
                hi = pi - 1
            else:
                lo = pi + 1

        return -1

        

s = Solution()
nums = [-1,0,3,5,9,12]
target = 9
assert (s.search(nums=nums, target=target) == 4) 