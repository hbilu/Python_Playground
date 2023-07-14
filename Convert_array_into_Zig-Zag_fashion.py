"""
Given an array arr of distinct elements of size N, the task is to rearrange the elements of the array in a zig-zag fashion so that the converted array should be in the below form:
arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n].
NOTE: If your transformation is correct, the output will be 1 else the output will be 0.

Example :
Input:
N = 7
Arr[] = {4, 3, 7, 8, 6, 2, 1}
Output: 3 7 4 8 2 6 1
Explanation: 3 < 7 > 4 < 8 > 2 < 6 > 1

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""

# first way:
def zigZag(self, arr, n):
    for i in range(0, n - 1, 1):
        if i % 2 == 0 and arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        elif i % 2 == 1 and arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

# second way:
def zigZag(self, arr, n):
    for i in range(0, n - 1, 1):
        if i % 2 == 0:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        else:
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]