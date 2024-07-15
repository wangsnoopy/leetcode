class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # boundary to avoid visiting
        n = len(grid)

        # set 1 because we only want to count water
        grid.append([1]*n)
        for row in grid:
            row.append(1)
        dist = defaultdict(int)
        que = [] ; head = 0
        # initial land with distance = 0, dist to record the distance and the visit point
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dist[(i, j)] = 0
                    que.append((i, j))
        
        # edge case, if there is no land or no water
        if len(dist) == 0 or len(dist) == n*n:
            return -1

        # count the longest dist
        # start from the land

        while head < len(que):
            # current row, column
            r, c = que[head]
            head += 1
            # distance to next water
            d = dist[(r,c)] + 1
            # check all the possible point
            for nr, nc in ((r - 1, c),(r + 1, c), (r, c - 1),(r, c + 1)):
                if grid[nr][nc] == 0 and (nr, nc) not in dist:
                    dist[(nr, nc)] = d
                    que.append((nr, nc))
        
        return dist[que[-1]]