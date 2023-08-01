class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        String[] words = paragraph.toLowerCase().replaceAll("[^a-z0-9]", " ").split(" ");
        HashMap<String, Integer> counter = new HashMap<>();

        for(String word: words) {
            if(word.equals(""))
                continue;
            if(counter.containsKey(word))
                counter.put(word, counter.get(word) + 1);
            else
                counter.put(word, 1);
        }

        Set<String> keys = counter.keySet();
        int max = 0;
        String max_word = "";

        for(String key: keys) {
            if(!isIn(key, banned) && max < counter.get(key)) {
                max = counter.get(key);
                max_word = key;
            }
        }
        
        return max_word;
    }

    public boolean isIn(String key, String[] banned) {
        for(String word: banned) {
            if(key.equals(word))
                return true;
        }
        return false;
    }
}