class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols= len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        n_islands = 0
        def domi_reversi(r, c):
            if r < 0 or c < 0 or r>rows-1 or c>cols-1 or grid[r][c] == '0':
                return
            else:
                grid[r][c] = '0'
                for li, co in directions:
                    domi_reversi(r+li, c+co)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    domi_reversi(r, c)
                    n_islands += 1
        return n_islands
