class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()

        self.col_len = len(grid)
        self.row_len = len(grid[0])

        count = 0
        for i in range(self.col_len):
            for j in range(self.row_len):
                if grid[i][j] == "1":
                    count += 1
                    grid[i][j] = "x"
                    grid = self.search_neighbours(grid, i, j)
        return count

    def search_neighbours(self, grid: List[List[str]], i: int, j: int) -> List[List[str]]:
        queue = deque()
        queue.append((i, j))
        while queue:
            i, j = queue.popleft()
            print(i, j)
            if i-1 >= 0:
                if grid[i-1][j] == "1":
                    queue.append((i-1, j))
                    grid[i-1][j] = "x"
            if i+1 < self.col_len:
                if grid[i+1][j] == "1":
                    queue.append((i+1, j))
                    grid[i+1][j] = "x"
            if j-1 >= 0:
                if grid[i][j-1] == "1":
                    queue.append((i, j-1))
                    grid[i][j-1] = "x"
            if j+1 < self.row_len:
                if grid[i][j+1] == "1":
                    queue.append((i, j+1))
                    grid[i][j+1] = "x"
        return grid