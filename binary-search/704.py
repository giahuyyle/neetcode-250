class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)
        mid = (h + l) // 2

        while l < h:
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                h = mid
            mid = (h + l) // 2

        return -1