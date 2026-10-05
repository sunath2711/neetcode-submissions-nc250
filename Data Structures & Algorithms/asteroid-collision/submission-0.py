class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        mystack = []
        for a in asteroids:
            while mystack and mystack[-1] > 0 and a<0:
                diff = mystack[-1] + a

                if diff < 0:
                    mystack.pop()

                elif diff > 0:
                    a = 0
                    break
                else:
                    mystack.pop()
                    a = 0
                    break
            if a!=0:
                mystack.append(a)
        
        return mystack



        