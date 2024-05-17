'''
Given an array, rotate the array by one position in clock-wise direction.

Example 1: Input: N = 5, A[] = {1, 2, 3, 4, 5}
            Output: 5 1 2 3 4

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1<=N<=105
0<=a[i]<=105

'''

# first way
def rotate(arr, n):
    for i in range(n - 1):
        arr.append(arr.pop(0))
    return arr

# second way
def rotate(arr, n):
    arr[:] = arr[n - 1:] + arr[:n - 1]
    return arr

# third way
import numpy as np
def rotate( arr, n):
    arr = np.roll(arr, 1)
    return arr

# fourth way
