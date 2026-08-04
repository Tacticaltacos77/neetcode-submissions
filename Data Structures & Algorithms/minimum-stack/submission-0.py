class MinStack:

    def __init__(self):
        self.stack = []
        self.length =0
        self.minimum = []

    def push(self, val: int) -> None:
        if self.length ==0:
            self.minimum.append(val)
        else:
            if val <= self.minimum[-1]:
                self.minimum.append(val)
        self.length+=1
        self.stack.append(val)

    def pop(self) -> None:
        p_val = self.stack.pop()
        if self.minimum[-1] ==p_val:
            self.minimum.pop()
        self.length-=1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
