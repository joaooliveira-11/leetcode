from typing import List

def maxProfit(prices: List[int]) -> int:
    max_profit, min_price = 0, float('inf')

    for p in prices:
        if p < min_price:
            min_price = p
        
        max_profit = max(max_profit, p - min_price)

    return max_profit

if __name__ == "__main__":
    print(maxProfit(prices = [10,1,5,6,7,1]))
    print(maxProfit(prices = [10,8,7,5,2]))