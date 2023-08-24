class Solution {
    public void sortColors(int[] nums) {
        int[] count = new int[3];
        int[] result = new int[nums.length];
        
        for(int num: nums)
            count[num]++;
        
        for(int i=1; i<3; i++)
            count[i] += count[i - 1];
        
        for(int i=nums.length-1; i>=0; i--)
            result[--count[nums[i]]] = nums[i];

        for(int i=0; i<nums.length; i++)
            nums[i] = result[i];
    }
}
class Solution {
    public void sortColors(int[] nums) {
        int red = 0, white = 0, blue = nums.length - 1;
        
        while(white <= blue) {
            if(nums[white] < 1) {
                swap(nums, red, white);
                red++;
                white++;
            } else if(nums[white] > 1) {
                swap(nums, white, blue);
                blue--;
            } else {
                white++;
            }
        }
    }
    public void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
}