def uniquePaths(self, m: int, n: int) -> int:
        # cause only can do right or down, 
        # so it cost 1 to meet the end at the right and down bondary
        # each node have x path to meet the end, 
        # where x is the right and down neighbor of the node
        # calculate from left to right, down to top

        # down boundary
        row = [1] * n

        # calculate

        # down to top
        # m - 1: because we already done the bottom row
        for i in range(m - 1):
            # this is a row that use to calculate
            newRow = [1] * n
            # start from every second last value in each row
            # cause the last el always be 1
            # ex: n = 7, [0 1 2 3 4 5 6], start from index 5
            for j in range(n - 2, -1, -1):
                # node value will be right node + down node
                # right node index: j + 1
                # down row index: j, same as the index we want to calculate
                newRow[j] = newRow[j + 1] + row[j]
            # update new row, casue we calculate down to top
            row = newRow
        # return the start point
        return row[0]