"""
Given an Integer N and a list arr. Sort the array using bubble sort algorithm.

Example:    Input: N = 10, arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
            Output: 1 2 3 4 5 6 7 8 9 10

Expected Time Complexity: O(N^2).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 103
1 <= arr[i] <= 103
"""

class Solution:
    def bubbleSort(self,arr, n):
        for i in range(0,n,1):
            for j in range(0,n-i-1,1):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]