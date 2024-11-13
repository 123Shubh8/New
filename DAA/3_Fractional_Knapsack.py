def fractional_knapsack():
    # Get inputs from the user
    n = int(input("Enter the number of items: "))
    weights = []
    values = []

    print("Enter the weights of the items:")
    for _ in range(n):
        weights.append(int(input()))

    print("Enter the values of the items:")
    for _ in range(n):
        values.append(int(input()))

    capacity = int(input("Enter the capacity of the knapsack: "))

    res = 0
    # Pair : [Weight, Value]
    for pair in sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True):
        if capacity <= 0:  # Bag is fully filled
            break
        if pair[0] > capacity:  # Partial item
            res += int(capacity * (pair[1] / pair[0]))  # Fill the bag with a fraction
            capacity = 0
        elif pair[0] <= capacity:  # Full item
            res += pair[1]
            capacity -= pair[0]

    print("Maximum value in the knapsack:", res)


if __name__ == "__main__":
    fractional_knapsack()
