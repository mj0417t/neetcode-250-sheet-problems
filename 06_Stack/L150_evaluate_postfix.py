class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack=[]
        for op in tokens:
            if op=='+':
                a=stack.pop()
                b=stack.pop()
                stack.append(b+a)
            elif op=='*':
                a=stack.pop()
                b=stack.pop()
                stack.append(b*a)
            elif op=='-':
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            elif op=='/':
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(op))
        return stack.pop()
if __name__=='__main__':
    # tokens1 = ["2","1","+","3","*"]
    # tokens2 = ["4","13","5","/","+"]
    tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    sol=Solution()
    # print(sol.evalRPN(tokens1))
    # print(sol.evalRPN(tokens2))
    print(sol.evalRPN(tokens3))