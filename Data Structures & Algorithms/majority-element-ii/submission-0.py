class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_dict = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in my_dict:
                my_dict[nums[i]] += 1
            else:
                my_dict[nums[i]] = 1

        print(my_dict)
        return [key for key, value in my_dict.items() if value > (n//3)]
        
        

        