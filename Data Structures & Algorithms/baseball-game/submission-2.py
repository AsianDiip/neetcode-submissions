class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores_stack = []

        for operation in operations:
            if operation == '+':
                scores_stack.append(scores_stack[-2] + scores_stack[-1])
            elif operation == 'D':
                scores_stack.append(scores_stack[-1] * 2)
            elif operation == 'C':
                scores_stack.pop()
            else:
                scores_stack.append(int(operation))
        
        return sum(scores_stack)