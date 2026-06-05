class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                if (isPalindrome(left + 1, right)):
                    return True
                else:
                    return isPalindrome(left, right - 1)
            
            left += 1
            right -= 1
        
        return True
