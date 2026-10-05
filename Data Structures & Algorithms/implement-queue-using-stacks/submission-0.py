class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []       

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop()) # Fixed self.
        
        # Step 2: Return the popped value
        return self.output_stack.pop()

    def peek(self) -> int:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        
        # Step 2: Read the top without removing it
        return self.output_stack[-1]

    def empty(self) -> bool:
        return len(self.input_stack) == 0 and len(self.output_stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()