class Solution {
    public boolean isValid(String s) {
        Map<String, String> pairs = new HashMap<>();
        Deque<String> stack = new ArrayDeque<>(s.length());

        pairs.put(")", "(");
        pairs.put("}", "{");
        pairs.put("]", "[");

        for(String p: s.split("")) {
            if(pairs.containsValue(p))
                stack.push(p);
            else {
                if(stack.size() > 0 && pairs.get(p).equals(stack.peek()))
                    stack.pop();
                else
                    return false;
            }
        }

        if(stack.size() > 0)
            return false;
        else
            return true;
    }
}