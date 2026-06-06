class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        prev = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[prev]:
                prev = i
                nums[count] = nums[i]
                count += 1
        
        return count