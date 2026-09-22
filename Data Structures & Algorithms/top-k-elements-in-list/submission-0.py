class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                my_dict[nums[i]] += 1
            else:
                my_dict[nums[i]] = 1

        highest_k_keys = sorted(my_dict, key=my_dict.get , reverse=True)[:k]

        return highest_k_keys
        