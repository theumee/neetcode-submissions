class Solution {
    public int maxProfit(int[] prices) {
    int minPrice = Integer.MAX_VALUE; // Initialize minPrice to maximum value
        int maxProfit = 0; // Initialize maxProfit to 0
        
        for (int price : prices) {
            // Update minPrice to the lowest price seen so far
            minPrice = Math.min(minPrice, price);
            // Calculate the potential profit
            int profit = price - minPrice;
            // Update maxProfit if the current profit is greater
            maxProfit = Math.max(maxProfit, profit);
        }
        
        return maxProfit; //
    }
}
