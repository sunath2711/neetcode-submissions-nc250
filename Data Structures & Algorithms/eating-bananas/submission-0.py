class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            
            # Calculate total hours needed at speed 'mid'
            hours_needed = sum((p + mid - 1) // mid for p in piles)
            
            if hours_needed <= h:
                # Speed mid is fast enough, try to find a smaller speed
                right = mid
            else:
                # Speed mid is too slow, increase speed
                left = mid + 1
                
        return left
        