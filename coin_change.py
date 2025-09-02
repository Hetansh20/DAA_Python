def coin_change(coins, amount):
    # Create a list to store the minimum number of coins for each amount from 0 to amount.
    # Initialize with a value larger than any possible number of coins (e.g., amount + 1).
    dp = [amount + 1] * (amount + 1)

    # Base case: 0 coins are needed to make an amount of 0.
    dp[0] = 0

    # Iterate through all amounts from 1 to the target amount.
    for i in range(1, amount + 1):
        # For each amount, iterate through all coin denominations.
        for coin in coins:
            if i >= coin:
                # If the current amount is greater than or equal to the coin value,
                # we can potentially use this coin.
                # The number of coins would be 1 (the current coin) + the minimum coins
                # needed for the remaining amount (i - coin).
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[amount] is still the initial large value, it means the amount cannot be formed.
    if dp[amount] > amount:
        return -1
    else:
        return dp[amount]

coins = [1, 5, 6, 8]
amount = 11
min_coins = coin_change(coins, amount)
if min_coins != -1:
    print(f"The minimum number of coins to make {amount} is: {min_coins}")
else:
    print(f"It's not possible to make {amount} with the given coins.")