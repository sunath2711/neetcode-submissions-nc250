class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        n = len(people)
        i,j = 0,n-1

        people.sort()

        while i <=j:
            curr_wt = people[i] + people[j]
            if curr_wt <= limit:
                i+=1
            j-=1
            boats+=1
        
        return boats
            
        