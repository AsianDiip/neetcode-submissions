class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        prefix = [0] * nums_len
        suffix = [0] * nums_len

        product = 1
        for i in range(0, nums_len):
            prefix[i] = product
            product *= nums[i]
        
        product = 1
        for i in range(nums_len - 1, -1, -1):
            suffix[i] = product
            product *= nums[i]
        
        ans = []
        for i in range(0, nums_len):
            ans.append(suffix[i] * prefix[i])
        
        return ans
