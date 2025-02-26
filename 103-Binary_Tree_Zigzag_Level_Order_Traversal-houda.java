class Solution {
    public int numIslands(char[][] grid) {
        if(grid==null || grid.length==0 || grid[0]==null) return 0;

        int rows = grid.length;
        int cols = grid[0].length;
        int numIslands = 0;
        int[][] directions = {{0,1},{0,-1},{1,0},{-1,0}};
        Queue<int[]> q = new LinkedList<>();

        for(int r =0; r<rows;r++) {
            for(int c =0; c<cols; c++) {
                if(grid[r][c]=='1'){
                    numIslands++;
                    q.offer(new int[]{r, c});
                    grid[r][c] = '0';

                    while(!q.isEmpty()) {
                        int[] pos = q.poll();

                        int x = pos[0];
                        int y = pos[1];

                        for (int[] dir : directions) {
                            int newX = x+dir[0];
                            int newY = y+dir[1];
                            if(newX >= 0 && newX < rows && newY >=0 && newY < cols) {
                                if(grid[newX][newY] == '1') {
                                    q.offer(new int[]{newX,newY});
                                    grid[newX][newY] = '0';
                                }
                            }
                        }

                    }
                }
                
            }
        }
        return numIslands;

    }
}
