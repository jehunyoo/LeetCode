class Solution {
    public String longestPalindrome(String s) {
        String answer = "";
        for(int mid=0; mid<s.length(); mid++) {
            String str = findPalindrome(s, mid - 1, mid + 1);
            if(answer.length() < str.length())
                answer = str;
            if(mid + 1 < s.length() && s.charAt(mid) == s.charAt(mid + 1)) {
                str = findPalindrome(s, mid - 1, mid + 2);
                if(answer.length() < str.length())
                    answer = str;
            }
        }

        return answer;
    }

    public String findPalindrome(String s, int left, int right) {
        while(0 <= left && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return s.substring(left + 1, right);
    }
}