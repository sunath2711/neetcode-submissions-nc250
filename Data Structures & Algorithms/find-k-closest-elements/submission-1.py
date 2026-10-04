class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #think of it is a subarray to be foind out instead of numbers
        #this was  2 pointer and contiguous subarray logic works, the one farther from x , side we keep moving
        n = len(arr)
        left,right = 0,n-1

        while right - left + 1 > k:
            if (abs(arr[left]-x)) > (abs(arr[right]-x)):
                left+=1
            else:
                right-=1
        
        return arr[left:right+1]

        