class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for j in t:
            if j in dic:
                dic[j] -= 1
            else:
                return False

        return all(value == 0 for value in dic.values())                         
        