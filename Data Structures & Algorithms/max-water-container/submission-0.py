class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        left, right = 0, len(heights)-1
        while left < right:
            current = min(heights[left], heights[right])*(right-left)
            if current > best:
                best = current
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return best
