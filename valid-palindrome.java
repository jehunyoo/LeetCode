class Solution {
    public boolean isPalindrome(String s) {
        char[] arr = new char[s.length()];
        int index = 0;
        char ch;
        s = s.toLowerCase();
        for(int i=0; i<s.length(); i++) {
            ch = s.charAt(i);
            if(('0' <= ch && ch <= '9') || ('a' <= ch && ch <= 'z')) {
                arr[index++] = ch;
            }
        }
        boolean answer = true;
        int left = 0, right = index - 1;
        while(left < right) {
            if(arr[left] != arr[right]) {
                answer = false;
                break;
            }
            left++;
            right--;
        }

        return answer;
    }
}