class Solution {
    public int[] twoSum(int[] numbers, int target) {
        for(int i=0; i<numbers.length - 1; i++) {
            int t = target - numbers[i];
            int left = 0, right = numbers.length -1;
            int mid = -1;
            while(left <= right) {
                mid = left + (right - left) / 2;
                if(numbers[mid] == t) {
                    if(mid != i)
                        return new int[]{i + 1, mid + 1};
                    else if(numbers[mid] == numbers[mid + 1])
                        return new int[]{i + 1, mid + 2};
                }
                else if(numbers[mid] < t) {
                    left = mid + 1;
                } else {
                    right = mid -1;
                }
            }
        }
        return new int[]{};
    }
}