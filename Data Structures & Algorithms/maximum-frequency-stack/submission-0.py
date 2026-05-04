class FreqStack:

    def __init__(self):
        self.stack = []
        self.s = defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.s[val] +=1

    def pop(self) -> int:
        max_value = max(self.s.values())
        max_keys = [key for key, value in self.s.items() if value == max_value]
        h = set(max_keys)
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i] in h:
                self.s[self.stack[i]] -=1
                return self.stack.pop(i)


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()