class Solution(object):
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []
        
        p_num = [0] * 26
        s_num = [0] * 26
        
        for char in p:
            p_num[ord(char) - 97] += 1
        
        result = []
        for i in range(len(s)):
            s_num[ord(s[i]) - 97] += 1
            
            if i >= len(p):
                s_num[ord(s[i - len(p)]) - 97] -= 1
            
            if s_num == p_num:
                result.append(i - len(p) + 1)
        
        return result