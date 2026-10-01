class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(i,j):
            start,end = i,j
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1    
            return True
        
        i,j = 0,len(s)-1
        while i < j:
            if s[i] != s[j]:
                return isPalindrome(i,j-1) or isPalindrome(i+1,j)
            i+=1
            j-=1
        return True



        