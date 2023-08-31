class Solution {
    public int hammingDistance(int x, int y) {
        if(x == 0 && y == 0)
            return 0;
        return (x ^ y) % 2 + hammingDistance(x >> 1, y >> 1);
    }
}