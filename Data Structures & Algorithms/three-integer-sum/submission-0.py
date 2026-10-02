class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
# n1+n2+n3 = 0 ; n2+n3 = -n1 ; 2 piositive nos cant be giving -ive value
            if nums[i] > 0: #once we have the ascending order set
                break #if even the smallest is positive, then 2 larger number than that cannot sum to its negative 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.twoSum(nums,i,res)
        return res

    def twoSum(self,nums,i,res):
        left = i+1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right] 

            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                left+=1
                right-=1
                # these two to skip duplicate triplets
                while left < right and nums[left] == nums[left-1]:
                    left+=1
                
                while left < right and nums[right] == nums[right+1]:
                    right-=1
            
            elif total < 0:
                left += 1
            else:
                right -= 1 





        