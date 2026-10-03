class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxarea = 0
        n = len(heights)
        start,end = 0,n-1
        while start < end:
            curr_area = (end-start) * min(heights[start],heights[end])
            maxarea = max(maxarea,curr_area)
            if heights[start] > heights[end]:
                end-=1
            else:
                start+=1
        
        return maxarea

        