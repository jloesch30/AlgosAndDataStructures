"""
[1,2,3,5,6]
     h l 
       p
       
[1,3,4,6]
 h l    
target = 0

return the index of high + 1
target = 4

"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            pi = left + (right - left) // 2
            
            if target == nums[pi]:
                return pi
            
            if target < nums[pi]:
                right = pi - 1
            
            else:
                left = pi + 1
        
        return left

#         if right < 0:
#             return 0
#         if target <= nums[right]:
#             return right
    
#         return right + 1