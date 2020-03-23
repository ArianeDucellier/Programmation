def maxProfit(prices):
    """
    """
    buy = [prices[0]]
    sell = []
    for price in prices[1:]:
        # Do we buy?
        if price < min(buy):
            if len(sell) == 0:
                buy[0] = price
            else:
                buy.append(price)
        # Do we sell?
        for i in range(0, len(buy)):
            if price > buy[i]:
                if i + 1 > len(sell):
                    sell.append(price)
                else:
                    if price > sell[i]:
                        sell[i] = price
    profit = []
    if len(sell) == 0:
        return None
    else:
        for i in range(0, min(len(buy), len(sell))):
            profit.append(sell[i] - buy[i])
        return max(profit)
