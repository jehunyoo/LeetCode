class Solution {
    public int numIslands(char[][] grid) {
        int M = grid.length, N = grid[0].length;
        boolean[][] visited = new boolean[M][N];
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        int count = 0;

        for(int i=0; i<M; i++) {
            for(int j=0; j<N; j++) {
                if(grid[i][j] == '1' && !visited[i][j]) {
                    count++;
                    Deque<Pair> stack = new ArrayDeque<>();
                    stack.push(new Pair(i, j));
                    while(stack.size() > 0) {
                        Pair pair = stack.pop();
                        int x = pair.x, y = pair.y;
                        if(!visited[x][y]) {
                            visited[x][y] = true;
                            for(int d=0; d<4; d++) {
                                int nx = x + dx[d], ny = y + dy[d];
                                if(0 <= nx && nx < M && 0 <= ny && ny < N && !visited[nx][ny] && grid[nx][ny] == '1')
                                    stack.push(new Pair(nx, ny));
                            }
                        }
                    }
                }
            }
        }
        return count;
    }
}

class Pair {
    int x;
    int y;

    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }
}