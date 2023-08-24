class Solution {
    public boolean isAnagram(String s, String t) {
        int[] countS = new int['z' - 'a' + 1];
        int[] countT = new int['z' - 'a' + 1];

        for(char ch: s.toCharArray())
            countS[ch - 'a']++;
        for(char ch: t.toCharArray())
            countT[ch - 'a']++;
        
        for(int i=0; i<='z'-'a'; i++) {
            if(countS[i] != countT[i])
                return false;
        }
        return true;
    }
}