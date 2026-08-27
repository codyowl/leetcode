class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        The idea here is to get the smallest price and then check that with a maximum profit while traversing from left to right, causing picking up a random smallets price wont make sense if the smalles profit is at the last day of the list

        profit = current_price - minimum_profit

        if profit > maximum_profit:
            treat that as the maximum profile
        """

        # we are going to take the first element as minimum profit from the index
        minimum_profit = prices[0]
        # initiaing maximum profit as 0
        maximum_profit = 0

        # iterating the elemnts left to right
        for i in range(1, len(prices)):
            # we need to update the minimum profit if the current element is much lesser
            if prices[i] < minimum_profit:
                minimum_profit = prices[i]

            # here we are finding the current profit and we need to update when the current profit is gerater tha maxmimum profit like how we did for updating our minimum profit
            else:
                current_profit = prices[i] - minimum_profit    

                # here we are going to update    
                if current_profit > maximum_profit:
                    maximum_profit = current_profit

        return maximum_profit