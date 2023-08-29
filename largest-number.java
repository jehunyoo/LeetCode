import java.math.BigInteger;

class Solution {
    public String largestNumber(int[] nums) {
        for(int i=1; i<nums.length; i++) {
            for(int j=i; j>0; j--) {
                if(needSwap(nums[j - 1], nums[j])) {
                    int temp = nums[j];
                    nums[j] = nums[j - 1];
                    nums[j - 1] = temp;
                } else {
                    break;
                }
            }
        }

        String[] answer = new String[nums.length];
        for(int i=0; i<nums.length; i++) {
            answer[i] = String.valueOf(nums[i]);
        }
        
        BigInteger big = new BigInteger(String.join("", answer));
        return big.toString();
    }

    public boolean needSwap(int a, int b) {
        String A = String.valueOf(a);
        String B = String.valueOf(b);
        
        return (A+B).compareTo(B+A) < 0;
    }
}