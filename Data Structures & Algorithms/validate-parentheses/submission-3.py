class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        dicMap = {"}": "{", ")": "(", "]": "["}
        for c in s:
            if c =="{" or c=="[" or c=="(":
                stack.append(c)
            elif (c =="}" or c=="]" or c==")"):
                if len(stack)>0 and dicMap[c] ==stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack)==0