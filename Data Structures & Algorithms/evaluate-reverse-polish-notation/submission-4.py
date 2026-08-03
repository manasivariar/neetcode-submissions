class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y) 
                print(stack)

            elif i == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y-x) 
                print(stack)

            elif i == "*":
                x = stack.pop()
                y = stack.pop()
                stack.append(x*y) 

            elif i == "/":
                x = stack.pop()
                y = stack.pop()
                stack.append(int(y/x)) 
                print(stack)
            
            else:
                stack.append(int(i))

        return stack[-1]




        