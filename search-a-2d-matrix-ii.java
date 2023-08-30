class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int M = matrix.length, N = matrix[0].length;

        int row = 0;
        int col = N - 1;

        while(row < M && col >= 0) {
            if(matrix[row][col] == target)
                return true;
            else if(matrix[row][col] < target)
                row++;
            else if(matrix[row][col] > target)
                col--;
        }
        return false;
    }
}