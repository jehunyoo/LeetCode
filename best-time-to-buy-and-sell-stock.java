class Solution {
    public int maxProfit(int[] prices) {
        int min = 10000;
        int profit = 0;

        for(int price: prices) {
            if(price < min) {
                min = price;
            }
            profit = price - min > profit? price - min: profit;
        }

        return profit;
    }
}