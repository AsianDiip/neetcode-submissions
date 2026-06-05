class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)

        left = length - 1
        right = 0

        while right < left:
            if not s[left].isalnum():
                left -= 1
                continue
            if not s[right].isalnum():
                right += 1
                continue
            
            if s[right].upper() != s[left].upper():
                return False
            
            right += 1
            left -= 1

        return True