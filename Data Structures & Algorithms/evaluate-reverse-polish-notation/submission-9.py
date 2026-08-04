class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[int(tokens[0])]
        for v in tokens[1:]:
            new= 0
            if v not in ("+", "-", "*", "/"):
                stack.append(int(v))
            elif v =="+":
                v1 = stack.pop()
                v2 = stack.pop()
                new = v2+v1
                stack.append(new)
            elif v=="-":
                v1 = stack.pop()
                v2 = stack.pop()
                new = v2-v1
                stack.append(new)
            elif v =="*":
                v1 = stack.pop()
                v2 = stack.pop()
                new = v2*v1
                stack.append(new)
            elif v=="/":
                v1 = stack.pop()
                v2 = stack.pop()
                new = int(v2/v1)
                stack.append(new)
            
           
        return stack[-1]