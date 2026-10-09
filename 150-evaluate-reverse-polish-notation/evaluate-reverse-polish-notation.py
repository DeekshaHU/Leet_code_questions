class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack=[]
        for i in tokens:
            if i=='+':
                x=stack.pop()
                y=stack.pop()
                stack.append(x+y)
            elif i=='-':
                x=stack.pop()
                y=stack.pop()
                stack.append(y-x)
            elif i=='*':
                x=stack.pop()
                y=stack.pop()
                stack.append(x*y)
            elif i=='/':
                y=stack.pop()
                x=stack.pop()
                stack.append(int(x/y))
            else:
                stack.append(int(i))
        return stack[-1]
                                                                 
        