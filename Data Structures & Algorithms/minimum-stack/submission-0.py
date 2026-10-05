class MinStack:

    def __init__(self):
        self.mystack = [None] * 30005
        self.top_idx = -1  # Renamed from self.top to self.top_idx

    def push(self, val: int) -> None:
        if self.top_idx == -1:
            curr_min = val
        else:
            curr_min = min(self.mystack[self.top_idx][1], val)
            
        self.top_idx += 1
        self.mystack[self.top_idx] = (val, curr_min)
       
    def pop(self) -> None:
        self.top_idx -= 1

    def top(self) -> int:
        return self.mystack[self.top_idx][0]

    def getMin(self) -> int:
        return self.mystack[self.top_idx][1]
        
