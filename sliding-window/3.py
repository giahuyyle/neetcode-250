# brute force, O(n^2) where n is length of s
def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) < 2:
        return len(s)

    l = 0
    r = 1
    m = len(s)
    res = 1

    while l < r and r < m:
        curr = 1

        seen = set()
        seen.add(s[l])
        while r < m and s[r] not in seen:
            seen.add(s[r])
            curr += 1
            r += 1
        
        l += 1
        r = l+1
        res = max(curr, res)
    
    return res

# sliding window, O(n) where n is length of s
def lengthOfLongestSubstring1(self, s: str) -> int:
    left = max_length = 0
    char_set = set()
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length