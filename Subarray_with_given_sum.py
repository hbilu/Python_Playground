"""
Given an unsorted array A of size N that contains only non-negative integers,
find a continuous sub-array which adds to a given number S.
In case of multiple subarrays, return the subarray which comes first on moving from left to right.

The task:
The task is to complete the function subarraySum() which takes arr, N and S as input parameters
and returns an arraylist containing the starting and ending positions of the first such occurring subarray
from the left where sum equals to S.
The two indexes in the array should be according to 1-based indexing.
If no such subarray is found, return an array consisting only one element that is -1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Example:
    Input: N = 5, S = 12, A[] = {1,2,3,7,5}
    Output: 2 4
Explanation: The sum of elements from 2nd position to 4th position is 12.
"""

class Solution:
    def subArraySum(self, arr, n, s):
        if s == 0:
            return [-1]
        sum2 = arr[0]
        start = 0
        end = 0
        while start < n and end < n:
            if sum2 == s:
                return start+1, end+1
            if sum2 > s:
                sum2 -= arr[start]
                start += 1
            else:
                end += 1
                if end >= n:
                    return [-1]
                sum2 += arr[end]
        return [-1]
