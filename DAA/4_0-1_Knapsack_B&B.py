import heapq

# A class to represent a node in the branch and bound tree
class KnapsackNode:
    def __init__(self, level, profit, weight, bound):
        self.level = level  # level of the node in the tree
        self.profit = profit  # total profit of the items selected so far
        self.weight = weight  # total weight of the items selected so far
        self.bound = bound  # upper bound of the profit that can be obtained from this node
    
    def __lt__(self, other):
        # For max-heap, reverse the comparison
        return self.bound > other.bound

def knapsack_branch_bound(W, wt, val, n):
    # Priority Queue (max-heap) to store the nodes
    pq = []
    
    # Initial node (starting with level -1, profit 0, weight 0, and bound calculated)
    root = KnapsackNode(-1, 0, 0, calculate_bound(0, 0, W, wt, val, n))
    heapq.heappush(pq, root)
    
    max_profit = 0  # Store the maximum profit found so far
    
    while pq:
        # Get the node with the best bound (max-heap)
        node = heapq.heappop(pq)
        
        # If we reach a valid node, we update the maximum profit
        if node.level == n - 1:
            continue
        
        # Explore the next level in the tree (take or don't take the next item)
        level = node.level + 1
        profit_with_item = node.profit + val[level]
        weight_with_item = node.weight + wt[level]
        
        # Case 1: Include the current item if it does not exceed capacity
        if weight_with_item <= W:
            if profit_with_item > max_profit:
                max_profit = profit_with_item
            bound = calculate_bound(profit_with_item, weight_with_item, W, wt, val, n)
            if bound > max_profit:
                heapq.heappush(pq, KnapsackNode(level, profit_with_item, weight_with_item, bound))
        
        # Case 2: Do not include the current item
        bound = calculate_bound(node.profit, node.weight, W, wt, val, n)
        if bound > max_profit:
            heapq.heappush(pq, KnapsackNode(level, node.profit, node.weight, bound))
    
    return max_profit

def calculate_bound(profit, weight, W, wt, val, n):
    if weight >= W:
        return 0  # No profit if weight exceeds capacity
    
    bound = profit
    total_weight = weight
    j = weight
    
    # Try to take as many items as possible, including fractions of items
    while j < n and total_weight + wt[j] <= W:
        total_weight += wt[j]
        bound += val[j]
        j += 1
    
    # If there is still space, include a fraction of the next item
    if j < n:
        bound += (W - total_weight) * val[j] / wt[j]
    
    return bound

def solve_knapsack():
    # User input for the number of items
    n = int(input("Enter the number of items: "))
    
    # User input for values and weights of the items
    val = []
    wt = []
    
    for i in range(n):
        value = int(input(f"Enter value of item {i+1}: "))
        weight = int(input(f"Enter weight of item {i+1}: "))
        val.append(value)
        wt.append(weight)
    
    # User input for the capacity of the knapsack
    W = int(input("Enter the capacity of the knapsack: "))
    
    # Call the knapsack_branch_bound function to compute the maximum value
    result = knapsack_branch_bound(W, wt, val, n)
    print("Maximum value in Knapsack =", result)

if __name__ == "__main__":
    solve_knapsack()
