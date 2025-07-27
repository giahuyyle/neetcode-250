class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        end = -1
        largest = nums[0]

        for i in range(1, len(nums)):
            if (largest > nums[i]):
                end = i
            else:
                largest = nums[i]

        start = 0
        smallest = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if (smallest < nums[i]):
                start = i
            else:
                smallest = nums[i]

        
        return (end - start + 1)