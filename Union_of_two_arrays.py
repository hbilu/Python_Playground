'''
Given two arrays a[] and b[] of size n and m respectively.
The task is to find the number of elements in the union between these two arrays.

Example:    Input: 5 3
                   1 2 3 4 5
                   1 2 3
            Output: 5
            Explanation: 1, 2, 3, 4 and 5 are the elements which comes in the union set of both arrays. So count is 5.

Constraints:
1 ≤ n, m ≤ 105
0 ≤ a[i], b[i] < 105

Expected Time Complexity : O(n+m)
Expected Auxilliary Space : O(n+m)
'''

class Solution:
    def doUnion(self,a,n,b,m):
        return len(set(a+b))