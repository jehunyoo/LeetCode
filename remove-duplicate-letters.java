class Solution {
    public String removeDuplicateLetters(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        Set<Character> used = new HashSet<>();
        Map<Character, Integer> counter = new HashMap<>();

        for(char ch: s.toCharArray()) {
            if(counter.containsKey(ch)) {
                counter.put(ch, counter.get(ch) + 1);
            } else {
                counter.put(ch, 1);
            }
        }

        for(char ch: s.toCharArray()) {
            counter.put(ch, counter.get(ch) - 1);
            if(used.contains(ch))
                continue;
            
            while(stack.size() > 0 && ch < stack.peek() && counter.get(stack.peek()) > 0) {
                used.remove(stack.pop());
            }
            stack.push(ch);
            used.add(ch);
        }

        String answer = "";
        while(stack.size() > 0) {
            answer += String.valueOf(stack.removeLast());
        }
        return answer;
    }
}