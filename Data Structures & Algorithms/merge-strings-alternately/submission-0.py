class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        pointer_one = 0
        pointer_two = 0

        ans = ""

        while pointer_one < len(word1) and pointer_two < len(word2):
            ans += word1[pointer_one]
            pointer_one += 1

            ans += word2[pointer_two]
            pointer_two += 1
        
        if pointer_one < len(word1):
            ans += word1[pointer_one::]
        if pointer_two < len(word2):
            ans += word2[pointer_two::]
        
        return ans