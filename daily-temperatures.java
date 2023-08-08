class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Deque<Pair> stack = new ArrayDeque<>(temperatures.length);
        int[] answer = new int[temperatures.length];

        for(int i=0; i<temperatures.length; i++) {
            Pair pair = new Pair(i, temperatures[i]);
            while(stack.size() > 0 && stack.peek().temperature < temperatures[i]) {
                Pair p = stack.pop();
                answer[p.index] = i - p.index;
            }
            stack.push(pair);
        }

        return answer;
    }
}

class Pair {
    int index;
    int temperature;

    Pair(int index, int temperature) {
        this.index = index;
        this.temperature = temperature;
    }
}