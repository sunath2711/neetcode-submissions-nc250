class Solution:
    def trap(self, height: List[int]) -> int:
        #2 pointer apporach

        n = len(height)
        left,right = 0,n-1
        lmax,rmax = height[left], height[right]
        
        water = 0
        while left < right:
            if lmax < rmax:
                left+=1
                lmax = max(lmax,height[left])
                water += lmax - height[left]
                
            elif lmax >= rmax:
                right -= 1
                
                rmax = max(rmax,height[right])
                water += rmax - height[right]
            
        return water



        