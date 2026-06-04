class Solution:
    def isValid(self, s: str) -> bool:
        brakets = {')': '('}
        
        opens = ['(', '{', '[']
        close = [')', '}', ']']

        open_stack = []

        for char in s:
            if char in opens:
                open_stack.append(char)
            else:
                if len(open_stack) == 0:
                    return False
                elif char == close[0] and open_stack.pop() != opens[0]:
                    return False
                elif char == close[1] and open_stack.pop() != opens[1]:
                    return False
                if char == close[2] and open_stack.pop() != opens[2]:
                    return False
        
        return len(open_stack) == 0
                