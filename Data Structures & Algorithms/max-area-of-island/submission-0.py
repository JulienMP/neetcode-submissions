class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        best = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def domi_reversi(r, c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0:
                return 0
            grid[r][c] = 0
            area = 1
            for li, co in directions:
                area += domi_reversi(r+li, c+co)
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = domi_reversi(r, c)
                    best = max(best, area)
        return best
