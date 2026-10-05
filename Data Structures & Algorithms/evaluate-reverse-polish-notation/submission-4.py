class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mystack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                num1 = mystack.pop()
                num2 = mystack.pop()
                mystack.append(num1 + num2)
            elif  tokens[i] == "-":
                num1 = mystack.pop()
                num2 = mystack.pop()
                mystack.append(num2 - num1)
            elif tokens[i] == "*":
                num1 = mystack.pop()
                num2 = mystack.pop()
                mystack.append(num1 * num2)
            elif tokens[i] == "/":
                num1 = mystack.pop()
                num2 = mystack.pop()
                mystack.append(int(num2 / num1))
            else:
                mystack.append(int(tokens[i]))
        return mystack[-1]