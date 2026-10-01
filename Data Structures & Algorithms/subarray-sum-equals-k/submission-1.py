class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        seen = {0:1}
        curr_sum = 0
        # curr_sum = any_older_sum + k 
        # any_older_sum = curr_sum - k 
        # we store each curr_sum in our dict and check if any older_sum already we have seen, if we have that means a 
        # sub array is possible with sum=k    
        for i in range(len(nums)):
            curr_sum += nums[i]
            any_older_sum = curr_sum - k
            if any_older_sum in seen:
                result += seen[any_older_sum]
            if curr_sum in seen:
                seen[curr_sum] += 1
            else:
                seen[curr_sum] = 1
        
        return result

        