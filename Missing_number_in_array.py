"""
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N.
Find the missing element.

The task:
Complete the function MissingNumber() that takes array and N as input parameters
and returns the value of the missing number.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""
class Solution:
    def MissingNumber(self, array, n):
        total = (n*(n+1))/2
        arr_sum = sum(array)
        return int(total-arr_sum)