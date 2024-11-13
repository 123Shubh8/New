def knapsack_dp(W, wt, val, n):
    # Create a 2D array to store the maximum value that can be obtained with a given weight and item count
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Fill the dp table in a bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                # If the item can be included, take the maximum of including or excluding it
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                # If the item cannot be included, take the value from the row above
                dp[i][w] = dp[i - 1][w]
    
    # The value in the bottom-right corner will be the result
    return dp[n][W]

def solve_knapsack():
    # User input for number of items
    n = int(input("Enter the number of items: "))
    
    # User input for values and weights of the items
    val = []
    wt = []
    
    for i in range(n):
        value = int(input(f"Enter value of item {i+1}: "))
        weight = int(input(f"Enter weight of item {i+1}: "))
        val.append(value)
        wt.append(weight)
    
    # User input for the capacity of the knapsack (after entering items)
    W = int(input("Enter the capacity of the knapsack: "))
    
    # Call the knapsack_dp function to compute the maximum value
    result = knapsack_dp(W, wt, val, n)
    print("Maximum value in Knapsack =", result)

if __name__ == "__main__":
    solve_knapsack()
