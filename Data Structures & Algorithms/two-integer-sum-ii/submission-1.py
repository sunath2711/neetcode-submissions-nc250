class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #thought about map but then read about O(1) so no extra space
        n = len(numbers)
        i,j = 0,n-1


        while i<j:
            the_sum = numbers[i] + numbers[j]
            if target == the_sum:
                return [i+1,j+1]
            elif target > the_sum:
                i+=1
            elif target < the_sum:
                j-=1
