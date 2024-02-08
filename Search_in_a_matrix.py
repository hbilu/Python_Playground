"""
Given a matrix mat[][] of size N x M, where every row and column is sorted in increasing order,
and a number X is given. The task is to find whether element X is present in the matrix or not.

Example: Input: N = 3, M = 3, mat[][] = 3 30 38  , X = 62
                                        44 52 54
                                        57 60 69
         Output: 0
         Explanation: 62 is not present in the matrix, so output is 0

Expected Time Complexity: O(N+M).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N, M <= 1005
1 <= mat[][] <= 10000000
1<= X <= 10000000
"""

# WİTH BİNARY SEARCH
class Solution:
	def matSearch(self,mat, N, M, X):
		start = 0
		end = M-1
		while (start<N and end>=0):
		    if mat[start][end]==X:
		        return 1
		    elif mat[start][end]>X:
		        end -= 1
		    elif mat[start][end]<X:
		        start += 1
		return 0