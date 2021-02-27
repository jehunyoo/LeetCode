class Solution:
    # DFS without visited: O(mn), O(1)
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        stack = []
        answer = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    stack.append((i, j))
                    answer += 1
                    while stack:
                        print(stack)
                        x, y = stack.pop()
                        if grid[x][y] == '1':
                            grid[x][y] = '0'
                            if x+1 < m and grid[x+1][y] == '1':
                                stack.append((x+1, y))
                            if y+1 < n and grid[x][y+1] == '1':
                                stack.append((x, y+1))
                            if 0 <= x-1 and grid[x-1][y] == '1':
                                stack.append((x-1, y))
                            if 0 <= y-1 and grid[x][y-1] == '1':
                                stack.append((x, y-1))
        return answer
    
    # DFS: O(mn), O(mn)
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        stack = []
        answer = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    stack.append((i, j))
                    answer += 1
                    while stack:
                        x, y = stack.pop()
                        if not visited[x][y]:
                            visited[x][y] = 1
                            if x+1 < m and grid[x+1][y] == '1' and not visited[x+1][y]:
                                stack.append((x+1, y))
                            if y+1 < n and grid[x][y+1] == '1' and not visited[x][y+1]:
                                stack.append((x, y+1))
                            if 0 <= x-1 and grid[x-1][y] == '1' and not visited[x-1][y]:
                                stack.append((x-1, y))
                            if 0 <= y-1 and grid[x][y-1] == '1' and not visited[x][y-1]:
                                stack.append((x, y-1))
        return answer