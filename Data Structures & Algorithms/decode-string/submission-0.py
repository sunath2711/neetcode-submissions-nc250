class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        curr_str = ""
        curr_num = 0

        for char in s:
            if char.isdigit():
                # Handle multi-digit numbers
                curr_num = curr_num * 10 + int(char)
                
            elif char == '[':
                # Save the state before entering the brackets
                num_stack.append(curr_num)
                str_stack.append(curr_str)
                # Reset current state for the inner string
                curr_str = ""
                curr_num = 0
                
            elif char == ']':
                # Pop the parent context
                k = num_stack.pop()
                prev_str = str_stack.pop()
                # Construct the decoded chunk and attach to parent context
                curr_str = prev_str + (curr_str * k)
                
            else:
                # Accumulate normal characters
                curr_str += char

        return curr_str
            