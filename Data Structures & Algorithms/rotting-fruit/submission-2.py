class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))

        max_time = 0
        while queue:
            i, j = queue.popleft()
            time = grid[i][j] - 2
            max_time = max(max_time, time)

            if i+1 < m and grid[i+1][j] == 1:
                grid[i+1][j] = 2 + time + 1
                queue.append((i+1, j))
            if i-1 >= 0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2 + time + 1
                queue.append((i-1, j))
            if j+1 < n and grid[i][j+1] == 1:
                grid[i][j+1] = 2 + time + 1
                queue.append((i, j+1))
            if j-1 >= 0 and grid[i][j-1] == 1:
                grid[i][j-1] = 2 + time + 1
                queue.append((i, j-1))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return max_time
        
