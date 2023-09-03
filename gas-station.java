class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        if(Arrays.stream(gas).sum() < Arrays.stream(cost).sum())
            return -1;

        int start = 0, fuel = 0;
        for(int i=0; i<gas.length; i++) {
            if(gas[i] + fuel < cost[i]) {
                fuel = 0;
                start = i + 1;
            } else {
                fuel += gas[i] - cost[i];
            }
        }

        return start;
    }
}