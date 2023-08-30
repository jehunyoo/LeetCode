class Solution {
    public int search(int[] nums, int target) {
        int mid = -1, pivot = -1;
        int left = 0, right = nums.length - 1;
        while(left < right) {
            mid = left + (right - left) / 2;
            if(nums[mid] == target)
                return mid;
            else if(nums[mid] <= nums[right]) {
                right = mid;
            } else if(nums[mid] > nums[right]) {
                left = mid + 1;
            }
        }
        
        pivot = left;

        if(target <= nums[nums.length - 1]) {
            left = pivot;
            right = nums.length - 1;
        } else if(target >= nums[0]) {
            left = 0;
            right = pivot - 1;
        }

        while(left <= right) {
            mid = left + (right - left) / 2;
            if(nums[mid] == target)
                return mid;
            else if(nums[mid] > target)
                right = mid - 1;
            else if(nums[mid] < target)
                left = mid + 1;
        }

        return -1;
    }
}