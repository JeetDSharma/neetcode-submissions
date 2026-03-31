class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ARITHMETIC_OPERATORS = ["+","-","/","*"]    
        stack = []
        for token in tokens:
            if token in ARITHMETIC_OPERATORS:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if token == '+':
                    stack.append(num1+num2)
                if token == '-':
                    stack.append(num1-num2)
                if token == "*":
                    stack.append(num1*num2)
                if token == "/":
                    stack.append(int(num1/num2))
            else:
                stack.append(token)
        
        return int(stack[-1])