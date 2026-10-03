class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
       # since there is restiction that at most theere can be 2 people on board, u need not think for best fit, main idea to eliminate the heaviest first
       count = 0
       n=len(people)
       people.sort()
       i,j = 0,n-1
       print(people)
       while i<=j:
        curr_wt = people[i] + people[j]
        if curr_wt <= limit:
            count+=1
            i+=1
            j-=1
        elif curr_wt > limit:
            count+=1
            j-=1
        
       return count
