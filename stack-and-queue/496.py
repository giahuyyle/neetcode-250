"""
Monotonic Stack
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hmap = {}

        for i in range(len(nums2) - 1, -1, -1):
            # while the stack is not empty or the top of the stack is smaller than
            # the number
            while stack and nums2[i] > stack[-1]:
                stack.pop()

            # if the stack is empty, map[num] = -1, i.e. no number
            if stack == []:
                hmap[nums2[i]] = -1
            
            else:
                hmap[nums2[i]] = stack[-1]
            
            stack.append(nums2[i])
        
        result = []
        for n in nums1:
            result.append(hmap[n])
                
        return result