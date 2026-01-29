class Solution:
    def gcdOfStrings(self, str1, str2) :
        lena = len(str1)
        lenb = len(str2)

        for i in range(lenb):
            tmp = lenb - i
            
            if lena % tmp == 0 and lenb % tmp == 0:
                pattern = str2[:tmp]
                if pattern * (lena // tmp) == str1 and pattern * (lenb // tmp) == str2:
                    return pattern
        
        return ""