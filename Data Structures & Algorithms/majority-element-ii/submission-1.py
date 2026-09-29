class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_map = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in my_map:
                my_map[nums[i]] += 1
            else:
                my_map[nums[i]] = 1
        
        return [key for key,value in my_map.items() if value > (n//3) ]