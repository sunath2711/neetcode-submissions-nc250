class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        right,left = n-1,0

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        
        return left


        