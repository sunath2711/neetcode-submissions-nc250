class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] not in seen:
                seen[nums[i]] = 1
                nums[j] = nums[i]
                j+=1

            elif nums[i] in seen:
                continue
        return j