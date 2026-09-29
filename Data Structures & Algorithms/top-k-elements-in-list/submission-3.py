class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        for i in range(len(nums)):
            if nums[i] in my_map:
                my_map[nums[i]] += 1
            else:
                my_map[nums[i]] = 1
        
        sorted_key_list = sorted(my_map.items(), key=lambda x: x[1], reverse=True)
        return [key for key,val in sorted_key_list[:k]]
        