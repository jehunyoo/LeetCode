class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] left = new int[nums.length + 1];
        int[] right = new int[nums.length + 1];
        int[] answer = new int[nums.length];

        left[0] = 1;
        for(int i=0; i<nums.length; i++) {
            left[i + 1] = nums[i] * left[i];
        }
        right[nums.length] = 1;
        for(int i=nums.length; i>0; i--) {
            right[i - 1] = nums[i - 1] * right[i];
        }
        for(int i=0; i<nums.length; i++) {
            answer[i] = left[i] * right[i + 1];
        }

        return answer;
    }
}