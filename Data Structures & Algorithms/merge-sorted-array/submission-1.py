class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m - 1
        right = n - 1
        curr = m + n - 1

        while left >= 0 and right >= 0:
            if nums1[left] >= nums2[right]:
                nums1[curr] = nums1[left]
                curr -= 1
                left -= 1
            else:
                nums1[curr] = nums2[right]
                right -= 1
                curr -= 1
        
        if right >= 0:
            for i in range (right, -1, -1):
                nums1[curr] = nums2[i]
                curr -= 1

        if left >= 0:
            for i in range (left, -1, -1):
                nums1[curr] = nums1[i]
                curr -= 1