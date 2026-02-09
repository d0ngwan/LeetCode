class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True
        
        ptr1 = 0
        for i in range(len(t)):
            if s[ptr1] == t[i]:
                ptr1 += 1
            
            if ptr1 == len(s):
                return True
        
        return ptr1 == len(s)