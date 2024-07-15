class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for row in grid: row.append(0)
        grid.append([0]* n)

        # return the size
        def land(r, c):
            que = [(r, c)]
            grid[r][c] = -1
            area = 0
            while que:
                r, c = que.pop()
                area += 1
                for nr, nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                    if grid[nr][nc] == 1:
                        que.append((nr,nc))
                        grid[nr][nc] = -1 # visited
            # end while
            return area
        
        largest = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    largest = max(largest, land(i, j))
        
        return largest