class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        foundNumbers = set([])
        for num in nums:
            if num in foundNumbers:
                return True
            else:
                foundNumbers.add(num)
        return False