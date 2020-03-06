def solve_greedy(coins, price):
    res = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        d, price = divmod(price, coin)
        res += d
    return res


def solve(coins, price):
    """This method ensure answer is correct!"""
    dp = [[0] * (price+1) for _ in range(len(coins))]
    for i, coin in enumerate(coins):
        for j in range(price+1):
            if i == 0:
                dp[i][j] = j // coin
            else:
                if j < coin: 
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coin]+1)
    return dp[-1][-1]


if __name__ == "__main__":
    japan_coins = [1, 5, 10, 50, 100, 500]
    special_coins = [1, 5, 8, 10, 50, 100, 500]
    price = 16

    print(f"(Greedy:japan_coins) price: {price}, ans: {solve_greedy(japan_coins, price)}")
    print(f"(Greedy:special_coins) price: {price}, ans: {solve_greedy(special_coins, price)}")
    print(f"(DP:japan_coins) price: {price}, ans: {solve(japan_coins, price)}")
    print(f"(DP:special_coins) price: {price}, ans: {solve(special_coins, price)}")





