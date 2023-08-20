class Trie {

    private Map<Character, Map> trie;

    public Trie() {
        trie = new HashMap<>();
    }
    
    public void insert(String word) {
        Map<Character, Map> node = trie;
        for(char ch: word.toCharArray()) {
            if(!node.containsKey(ch)) {
                Map<Character, Map> t = new HashMap<>();
                node.put(ch, t);
            }
            node = node.get(ch);
        }
        node.put(null, null);
    }
    
    public boolean search(String word) {
        Map<Character, Map> node = trie;
        for(char ch: word.toCharArray()) {
            if(!node.containsKey(ch))
                return false;
            node = node.get(ch);
        }
        if(node.containsKey(null))
            return true;
        else
            return false;
    }
    
    public boolean startsWith(String prefix) {
        Map<Character, Map> node = trie;
        for(char ch: prefix.toCharArray()) {
            if(!node.containsKey(ch))
                return false;
            node = node.get(ch);
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */