"""
Problem 14 - Longest Common Prefix
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in range(1, len(strs)):
            ans = ans[:min(len(ans), len(strs[i]))]
            for j in range(min(len(ans), len(strs[i]))):
                if ans[j] != strs[i][j]:
                    ans = ans[:j]
                    break
        return ans