class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True

        low = 1
        high = num // 2

        while low <= high:
            mid = (low + high) // 2

            if (num / mid) == mid:
                return True

            if (num / mid) < mid:
                high = mid - 1
            
            else:
                low = mid + 1
        
        return False