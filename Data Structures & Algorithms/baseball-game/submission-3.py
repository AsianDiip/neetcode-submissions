class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores_stack = []
        running_sum = 0

        for operation in operations:
            if operation == '+':
                running_sum += scores_stack[-2] + scores_stack[-1]
                scores_stack.append(scores_stack[-2] + scores_stack[-1])
            elif operation == 'D':
                running_sum += (scores_stack[-1] * 2)
                scores_stack.append(scores_stack[-1] * 2)
            elif operation == 'C':
                running_sum -= scores_stack.pop()
            else:
                scores_stack.append(int(operation))
                running_sum += int(operation)
        return running_sum
        