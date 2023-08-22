class Solution {
    public int maxSubArray(int[] nums) {
        for(int i=1; i<nums.length; i++)
            nums[i] += nums[i - 1] > 0? nums[i - 1]: 0;
        return maxArray(nums);
    }

    public int maxArray(int[] nums) {
        int max = nums[0];
        for(int num: nums) {
            max = Math.max(max, num);
        }
        return max;
    }

    public int maxSubArray(int[] nums) {
        int bestSum = Integer.MIN_VALUE;
        int currentSum = 0;
        for(int num: nums) {
            currentSum = Math.max(num, currentSum + num);
            bestSum = Math.max(bestSum, currentSum);
        }
        return bestSum;
    }
}