class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # create a map to store freq
        freqs = {}

        for num in arr1:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        
        # create a new array to return
        ans = []
        for num in arr2:
            ans += [num] * freqs[num]
            freqs[num] = -1
        
        # get the remaining elements
        remaining = []
        for num in freqs:
            if freqs[num] != -1:
                remaining += [num] * freqs[num]
                freqs[num] = -1
        
        remaining.sort()
        ans += remaining
        return ans