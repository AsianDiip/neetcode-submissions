class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        rects = [] #pair (height, index)

        for index, height in enumerate(heights):
            start = index
            while rects and rects[-1][0] > height:
                pop_height, pop_index = rects.pop()
                maxArea = max(maxArea, pop_height * (index - pop_index))
                start = pop_index
            rects.append((height, start))
        
        for h, i in rects:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea