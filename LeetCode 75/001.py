class Solution(object):
    def mergeAlternately(self, word1, word2):

        lena = len(word1)
        lenb = len(word2)

        ptr1 = 0
        ptr2 = 0
        str = ""

        while ( ptr1 < lena and ptr2 < lenb ) :
            str = str + word1[ptr1]
            str = str + word2[ptr2]
            ptr1 += 1
            ptr2 += 1
        
        if ( lena == ptr1 ) :
            while ( lenb > ptr2 ) :
                str = str + word2[ptr2]
                ptr2 += 1
        
        if ( lenb == ptr2 ) :
            while ( lena > ptr1) :
                str = str + word1[ptr1]
                ptr1 += 1
                
        return str