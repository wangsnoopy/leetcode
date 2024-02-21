class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # shift the grid k time
        # iterate k time
        # check the last el, and the last el in row
        while k > 0:
            cur = grid[0][0]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if j + 1 < len(grid[0]):
                        grid[i][j + 1], cur = cur, grid[i][j + 1]
                    elif j + 1 == len(grid[0]) and i != len(grid) - 1:
                        grid[i + 1][0], cur = cur, grid[i + 1][0]
                    else:
                        grid[0][0] = cur
            k -= 1
        
        return grid