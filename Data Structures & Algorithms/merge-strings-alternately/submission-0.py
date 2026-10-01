class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m1,m2 = len(word1),len(word2)
        new_word = ""

        if m1 > m2:
            for i in range(m2):
                new_word += word1[i] + word2[i]
            new_word += word1[i+1:]
        elif m2 > m1:
            for i in range(m1):
                new_word += word1[i] + word2[i]
            new_word += word2[i+1:]
        else:
            for i in range(m1):
                new_word += word1[i] + word2[i]

        return new_word
        