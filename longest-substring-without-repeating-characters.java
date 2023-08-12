class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        Set<Character> removeSet = new HashSet<>();
        int lp = 0, rp = 0;
        int answer = 0;
        while(s.length() > 0 && rp < s.length()) {
            char ch = s.charAt(rp);
            if(map.containsKey(ch)) {
                lp = map.get(ch) + 1;
                for(char key: map.keySet()) {
                    if(map.get(key) < lp)
                        removeSet.add(key);
                }
                for(char key: removeSet)
                    map.remove(key);
                removeSet.clear();
            } else {
                map.put(ch, rp++);
            }
            
            answer = answer < rp - lp? rp - lp: answer;
        }

        return answer;
    }
}