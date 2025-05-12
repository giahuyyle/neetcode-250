"""
PROBLEM 217 - Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example:
Input: nums = [1,2,3,1]
Output: true
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

"""
Time Complexity: O(n)
Space Complexity: O(n)
Where n is the number of elements in the input list.
"""