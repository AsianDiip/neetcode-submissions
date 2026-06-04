class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        buckets = [0] * 3
        for num in nums:
            buckets[num] += 1
        
        index = 0
        for num_index, num in enumerate(buckets):
            for i in range(0, num):
                nums[index] = num_index
                index += 1
        