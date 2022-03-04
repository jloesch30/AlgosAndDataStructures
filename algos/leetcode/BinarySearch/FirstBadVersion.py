from pickle import PickleBuffer


class Solution:
    """
    [1,2,3,4,5,6,7,8]

    Brute force solution:
    1.) iterate through the versions until you find the first bad version O(N)

    Binary search solution: O(log(n))
    pivot = 4
    left = 0
    right = len(versions) - 1 => 7

    1.) check if version 4 is bad
    2.) if bad, check the left subtree for another bad version
    3.) if not bad, we check the right subtree for a bad version
    4.) if we do not find a bad version in the left-subtree, the pivot is the lowest boundary
    """
    def isBadVersion(self, n: int):
        pass

    """
   My solution, did not work 
    """
    def firstBadVersion(self, n: int) -> int:
        left = 0
        high = len(n) - 1
        curr_lowest_bad = -1
        while left <= high:
            pivot = left + (high - left) // 2

            if self.isBadVersion(n[pivot]):
                curr_lowest_bad = n[pivot]
                high = pivot - 1

            if not self.isBadVersion(n[pivot]):
                left = pivot + 1

        return curr_lowest_bad

"""
Correct solution
"""
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        high = n
    
        while left < high:
            pivot = left + (high - left) // 2

            if isBadVersion(pivot):
                high = pivot

            else:
                left = pivot + 1

        return left
 
