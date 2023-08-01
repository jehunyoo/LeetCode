class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> anagrams = new HashMap<>();

        for(String str: strs) {
            char[] charr = str.toCharArray();
            Arrays.sort(charr);
            String s = new String(charr);
            if(anagrams.containsKey(s)) {
                anagrams.get(s).add(str);
            } else {
                ArrayList<String> group = new ArrayList<>();
                group.add(str);
                anagrams.put(s, group);
            }
        }
        List<List<String>> answer = new ArrayList<>();
        Set<String> keys = anagrams.keySet();
        for(String key: keys) {
            answer.add(anagrams.get(key));
        }

        return answer;
    }
}