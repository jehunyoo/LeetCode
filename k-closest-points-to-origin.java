class Solution {
    public int[][] kClosest(int[][] points, int k) {
        Arrays.sort(points, new Comparator<int[]>() {
            @Override
            public int compare(int[] p1, int[] p2) {
                int v1 = squareSum(p1[0], p1[1]);
                int v2 = squareSum(p2[0], p2[1]);
                return v1 > v2? 1: (v1 == v2? 0: -1);
            }
        });

        return Arrays.copyOfRange(points, 0, k);
    }
    public int squareSum(int x, int y) {
        return x*x + y*y;
    }
}