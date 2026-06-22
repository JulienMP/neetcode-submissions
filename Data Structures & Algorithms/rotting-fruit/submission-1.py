class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        min_time = 0
        #Detect the rotten fruits
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append(((r, c), 0))
        
        while queue:
            (r, c), temps = queue.popleft()
            for li, co in directions:
                if 0 <= r+li < rows and 0 <= c+co < cols and grid[r+li][c+co] == 1:
                    grid[r+li][c+co] = 2
                    min_time = temps+1
                    queue.append(((r+li, c+co), temps+1))

        #State impossible
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return min_time