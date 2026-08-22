class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        len_str = float('inf')

        for i in range(len(strs)):
            if len(strs[i]) < len_str:
                len_str = len(strs[i])

        # Compare characters column by column
        for j in range(len_str):
            target_char = strs[0][j]
            for i in strs:
                if i[j] != target_char:
                    return strs[0][:j]  # Return prefix up to mismatch

        return strs[0][:len_str]


        
        