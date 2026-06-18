class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0]*n
        suffix = [0]*n
        l, r = 0, n-1
        best_p, best_s = 0, 0
        area = 0
        while l < n:
            prefix[l] = best_p
            suffix[r] = best_s
            if height[l] > best_p:
                best_p = height[l]
            if height[r] > best_s:
                best_s = height[r]
            l += 1
            r -= 1
        for i in range(n):
            area += max(min(prefix[i], suffix[i]) - height[i], 0)
        return area