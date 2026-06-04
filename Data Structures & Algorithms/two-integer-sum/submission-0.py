from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for index, num in enumerate(nums):
            if (target - num) in values:
                return [values[target-num], index]

            values[num] = index