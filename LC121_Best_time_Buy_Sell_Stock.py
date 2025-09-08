# ------------------------Method 1 (Brute Force)----------------------------------------------------------------
prices = [7,2,1,5,6,4,8]
n = len(prices)
max_profit = 0

# Outer loop = pick buying day
for i in range(0, n):
    # Inner loop = pick selling day (after buying day)
    for j in range (i+1,n):
        # If selling price > buying price then profit possible
        if prices[j] > prices[i]:
            p = prices[j] - prices[i]  # profit = sell - buy
            max_profit = max(max_profit, p)  # store maximum profit seen so far

print(max_profit)  # final maximum profit


# TC (Time Complexity): O(n²) → har price ke liye baaki sab dekhna
# SC (Space Complexity): O(1) → sirf variables use ho rahe hain



# -------------------------Method 2 (Optimal – One Pass)----------------------------------------
prices = [9,2,8,5,4,6,12]
n = len(prices)
max_profit = 0 

# Start with a very large buying price so first price will be minimum
min_price = float("inf")

# Loop over each price only once
for i in range(0, n):
    # Step 1: update minimum price seen so far (best day to buy)
    min_price = min(min_price, prices[i])
    
    # Step 2: calculate profit if sold today (current price - min price)
    max_profit = max(max_profit, prices[i] - min_price)

print(max_profit)  # maximum profit after going through all days


# TC: O(n) → har price ek baar hi dekha
# SC: O(1) → sirf 2 variables (min_price & max_profit)