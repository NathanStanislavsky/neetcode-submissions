class Solution:
    def bfs(self, r, c, visited, grid):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        q = deque([(r, c)])
        visited.add((r, c))

        while q:
            curr_r, curr_c = q.popleft()

            for dr, dc in directions:
                new_row = curr_r + dr
                new_col = curr_c + dc

                if (0 <= new_row < len(grid) and 
                    0 <= new_col < len(grid[0]) and 
                    (new_row, new_col) not in visited and 
                    grid[new_row][new_col] == "1"):
                    q.append((new_row, new_col))
                    visited.add((new_row, new_col))

    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0

        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    numIslands += 1
                    self.bfs(r, c, visited, grid)
        
        return numIslands