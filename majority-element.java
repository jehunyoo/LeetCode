class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length/2];
    }
}

class Solution {
    public int majorityElement(int[] nums) {
        return mergeSort(nums)[nums.length / 2];
    }

    public int[] mergeSort(int[] nums) {
        if(nums.length == 1)
            return nums;
        
        int[] left = mergeSort(Arrays.copyOfRange(nums, 0, nums.length / 2));
        int[] right = mergeSort(Arrays.copyOfRange(nums, nums.length / 2, nums.length));

        int[] sorted = new int[nums.length];
        int index = 0, x = 0, y = 0;
        while(x < left.length && y < right.length) {
            if(left[x] < right[y]) {
                sorted[index++] = left[x++];
            } else {
                sorted[index++] = right[y++];
            }
        }
        while(x < left.length)
            sorted[index++] = left[x++];
        while(y < right.length)
            sorted[index++] = right[y++];

        return sorted;
    }
}