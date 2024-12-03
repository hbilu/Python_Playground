"""
You are given the weights and values of items, and you need to put these items in a knapsack of capacity capacity
to achieve the maximum total value in the knapsack. Each item is available in only one quantity.

In other words, you are given two integer arrays val[] and wt[], which represent the values and weights associated
with items, respectively. You are also given an integer capacity, which represents the knapsack capacity.
Your task is to find the maximum sum of values of a subset of val[] such that the sum of the weights of the
corresponding subset is less than or equal to capacity. You cannot break an item; you must either pick the entire item or leave it (0-1 property).

Examples :

    Input: capacity = 4, val[] = [1, 2, 3], wt[] = [4, 5, 1]
    Output: 3
    Explanation: Choose the last item, which weighs 1 unit and has a value of 3.

    Input: capacity = 3, val[] = [1, 2, 3], wt[] = [4, 5, 6]
    Output: 0
    Explanation: Every item has a weight exceeding the knapsack's capacity (3).

    Input: capacity = 5, val[] = [10, 40, 30, 50], wt[] = [5, 4, 6, 3]
    Output: 50
    Explanation: Choose the second item (value 40, weight 4) and the fourth item (value 50, weight 3)
                 for a total weight of 7, which exceeds the capacity. Instead, pick the last item (value 50, weight 3)
                for a total value of 50.

Expected Time Complexity: O(n*capacity).
Expected Auxiliary Space: O(n*capacity)

Constraints:
2 ≤ val.size() = wt.size() ≤ 103
1 ≤ capacity ≤ 103
1 ≤ val[i] ≤ 103
1 ≤ wt[i] ≤ 103
"""

# Dynamic Programming
class Solution:
    # Function to return max value that can be put in knapsack of capacity.
    def knapSack(self, capacity, val, wt):
        # Number of items
        n = len(val)
        # Create a DP table with dimensions (n+1) x (capacity+1)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        # Build the table
        for i in range(1, n + 1):
            for w in range(capacity + 1):
                # If the weight of the current item is more than the capacity, skip it
                if wt[i - 1] <= w:
                    # Item can be included or excluded
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wt[i - 1]] + val[i - 1])
                else:
                    # Item cannot be included, carry forward the previous value
                    dp[i][w] = dp[i - 1][w]
        # The last cell contains the maximum value we can achieve with the given capacity
        return dp[n][capacity]

# ------- Driver code of geekforgeeks -----------
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        # Read capacity
        capacity = int(input())
        values = list(map(
            int,
            input().strip().split()))  # Using 'values' instead of 'val'
        weights = list(map(
            int,
            input().strip().split()))  # Using 'weights' instead of 'wt'
        ob = Solution()
        print(ob.knapSack(capacity, values, weights))
        print("~")