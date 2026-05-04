class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
    
        for i in tokens:
            if i != '+' and i != '-' and i != '*' and i != '/':
                stack.append(int(i))
            else:
                if i == '+':
                    stack.append(stack.pop() + stack.pop())
                if i == '-':
                    a,b = stack.pop(), stack.pop()
                    stack.append(b-a)
                if i == '*':
                    stack.append(stack.pop() * stack.pop())
                if i == '/':
                    a,b = stack.pop(), stack.pop()
                    stack.append(int(float(b)/a))
        return stack[0]

        