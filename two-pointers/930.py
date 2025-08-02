def atMost(nums: List[int], goal: int) -> int:
    head, tail, total, result = 0, 0, 0, 0
    for head in range(len(nums)):
        total += nums[head]
        while total > goal and tail <= head:
            total -= nums[tail]
            tail += 1
        result += head - tail + 1
    return result

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return atMost(nums, goal)- atMost(nums, goal-1)