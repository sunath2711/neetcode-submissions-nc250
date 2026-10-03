class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0]*n
        right_max =[0]*n

        lm = left_max[0] = height[0] 
        rm = right_max[n-1] = height[n-1]
        
        for i in range(1,n):
            lm = max(lm,height[i])
            left_max[i] = lm
        
        for i in range(n-2,-1,-1):
            rm = max(rm,height[i])
            right_max[i] = rm

        #calcualt water above each tower 
        trapped_water_area = 0
        for i in range(1,n-1):
            trapped_water_area += (min(left_max[i],right_max[i]) - height[i])

        return trapped_water_area

          

        