class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {nums[0]:1}
        i,j = 1,1
        n = len(nums)
        while j<n:
            if nums[j] not in seen:
                nums[i] = nums[j]
                i+=1
                seen[nums[j]] = 1
            j+=1
        
        return i
            

        