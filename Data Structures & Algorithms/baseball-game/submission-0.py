class Solution:
    def calPoints(self, operations: List[str]) -> int:
        my_stack = []
        for i in range(len(operations)):
            if operations[i] == "C":
                my_stack.pop()
            elif operations[i] == "D":
                pr = int(my_stack[-1])*2
                my_stack.append(pr)
            elif operations[i] == "+":
                sm = int(my_stack[-1])+int(my_stack[-2])
                my_stack.append(sm)
            else:
                my_stack.append(int(operations[i]))                    
            print(my_stack)

        return sum(my_stack)
        