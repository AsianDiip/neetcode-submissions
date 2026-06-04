class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        right, left = 0, len(s) - 1

        while right < left:
            temp = s[right]
            s[right] = s[left]
            s[left] = temp
            right += 1
            left -= 1

