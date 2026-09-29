class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string += str(len(i)) + "#" + i
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j]!= "#":
                j+=1
            length=int(s[i:j])

            start = j+1
            end = j+length
            org_str = s[start:end+1]
            res.append(org_str)
            i=end+1


        return res


            
