"""
Given an array a[] of size N which contains elements from 0 to N-1,
you need to find all the elements occurring more than once in the given array.

The task:
Complete the function duplicates() which takes array a[] and n as input as parameters and
returns a list of elements that occur more than once in the given array in sorted manner.
If no such element is found, return list containing [-1].

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

Example:
    Input: N = 5, a[] = {2,3,1,2,3}
    Output: 2 3
"""

class Solution:
    def duplicates(self, arr, n):
        val = []
        for i in range(0, n, 1):
            x = arr[i] % n
            arr[x] = arr[x]+n
        for i in range(0, n, 1):
            if arr[i] >= n*2:
                val.append(i)
        if len(val) == 0:
            return [-1]
        else:
            return val
