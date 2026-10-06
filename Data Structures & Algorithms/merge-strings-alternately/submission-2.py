class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        new_str = ""
        m,n = len(word1),len(word2)

        if m > n:
            for i in range(n):
                new_str += word1[i] + word2[i]
            new_str += word1[i+1:m]
        
        elif n > m:
            for i in range(m):
                new_str += word1[i] + word2[i]
            new_str += word2[i+1:n]
        
        else:
            for i in range(m):
                new_str += word1[i] + word2[i]

        return new_str

        