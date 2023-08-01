"""
Given an array arr[ ] of length N consisting cost of N toys and an integer K depicting the amount with you.
Your task is to find maximum number of toys you can buy with K amount.

Example:
    Input: N = 7 K = 50 arr[] = {1, 12, 5, 111, 200, 1000, 10}
    Output: 4
"""

def toyCount(self, N, K, arr):
    arr.sort()
    count = 0
    for i in range(0, N, 1):
        if K >= arr[i]:
            count += 1
            K -= arr[i]
    return count