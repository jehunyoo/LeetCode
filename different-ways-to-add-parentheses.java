class Solution {
    public List<Integer> diffWaysToCompute(String expression) {
        if(isNumeric(expression)) {
            List<Integer> list = new ArrayList<>();
            list.add(Integer.parseInt(expression));
            return list;
        }

        List<Integer> list = new ArrayList<>();

        for(int i=0; i<expression.length(); i++) {
            switch (expression.charAt(i)) {
                case '+':
                    for(int num1: diffWaysToCompute(expression.substring(0, i))) {
                        for(int num2: diffWaysToCompute(expression.substring(i + 1))) {
                            list.add(num1 + num2);
                        }
                    }
                    break;
                case '-':
                    for(int num1: diffWaysToCompute(expression.substring(0, i))) {
                        for(int num2: diffWaysToCompute(expression.substring(i + 1))) {
                            list.add(num1 - num2);
                        }
                    }
                    break;
                case '*':
                    for(int num1: diffWaysToCompute(expression.substring(0, i))) {
                        for(int num2: diffWaysToCompute(expression.substring(i + 1))) {
                            list.add(num1 * num2);
                        }
                    }
                    break;
            }
        }

        return list;
    }

    public boolean isNumeric(String s) {
        for(int i=0; i<s.length(); i++) {
            char ch = s.charAt(i);
            if(!('0' <= ch && ch <= '9'))
                return false;
        }
        return true;
    }
}