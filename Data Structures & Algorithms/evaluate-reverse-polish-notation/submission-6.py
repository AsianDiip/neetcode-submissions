class Solution:
    def is_integer(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for token in tokens:
            if self.is_integer(token):
                nums.append(int(token))
            else:
                val_two = nums.pop()
                val_one = nums.pop()

                if (token == '+'):
                    nums.append(val_one + val_two)
                elif (token == '-'):
                    nums.append(val_one - val_two)
                elif (token == '*'):
                    nums.append(val_one * val_two)
                elif (token == '/'):
                    nums.append(int(val_one / val_two))
            
        return nums[-1]
                