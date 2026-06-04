def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    split = len(arr) // 2
    left = merge_sort(arr[:split])
    right = merge_sort(arr[split:])

    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    #left array index
    i = 0
    #right arr index
    j = 0

    ans = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1

    ans.extend(left[i:])
    ans.extend(right[j:])
    return ans

class Solution:


    def sortArray(self, nums: List[int]) -> List[int]:
        return merge_sort(nums)