"""
Given an array of N integers, and an integer K,
find the number of pairs of elements in the array whose sum is equal to K.

Example:
    Input: N = 4, K = 6, arr[] = {1, 5, 7, 1}
    Output: 2
    Explanation:  arr[0] + arr[1] = 1 + 5 = 6
                  and arr[1] + arr[3] = 5 + 1 = 6.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 105
1 <= K <= 108
1 <= Arr[i] <= 106
"""

class Solution:
    def getPairsCount(self, arr, n, k):
        map = {}
        count = 0
        for i in range(n):
            if k - arr[i] in map:
                count += map[k - arr[i]]
            if arr[i] in map:
                map[arr[i]] += 1
            else:
                map[arr[i]] = 1
        return count