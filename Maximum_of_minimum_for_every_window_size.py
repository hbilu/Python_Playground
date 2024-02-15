"""
Given an integer array. The task is to find the maximum of the minimum of every window size in the array.
Note: Window size varies from 1 to the size of the Array.

Example 1:

Input:
N = 7
arr[] = {10,20,30,50,10,70,30}
Output: 70 30 20 10 10 10 10
Explanation: First element in output indicates maximum of minimums of all windows of size 1. -> 70
             Second element in output indicates maximum of minimums of all windows of size 2. -> 30

Expected Time Complxity : O(N)
Expected Auxilliary Space : O(N)

Constraints:
1 <= N <= 105
1 <= arr[i] <= 106
"""

class Solution:
    def maxOfMin(self,arr,n):
        left = [-1] * n  # list to store the previous smaller elements
        right = [n] * n  # list to store the next smaller elements
        stack = []
        # Calculating the previous smaller element for each element in the array.
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        # left result -> [-1,0,1,2,-1,4,4]
        # Clearing the stack
        stack = []
        # Calculating the next smaller element for each element in the array.
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        # right result -> [7,4,4,4,7,6,7]
        result = [0] * (n + 1)
        # Calculate the maximum of the minimums for each window size.
        for i in range(n):
            # max window_size of an element between its previous and next smaller elements
            window_size = right[i] - left[i] - 1
            result[window_size] = max(result[window_size], arr[i])
        # result -> [0,70,30,20,0,0,0,10]
        # Fill gaps in the result with closest smaller element
        for i in range(n-1, 0, -1):
            result[i] = max(result[i], result[i+1])
        # result -> [70,70,30,20,10,10,10,10]
        return result[1:]