class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        OPENING_BRACKET = ['(', '{', '[']
        CLOSING_BRACKET = {')': '(',
        '}': '{',
        ']': '[' 
        }
        for bracket in s:
            if bracket in OPENING_BRACKET:
                stack.append(bracket)
            elif len(stack) == 0 or CLOSING_BRACKET[bracket] != stack[-1]:
                return False
            else:
                stack.pop()
        if stack:
            return False
        return True