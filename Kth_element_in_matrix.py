"""
Given a N x N matrix, where every row and column is sorted in non-decreasing order.
Find the kth smallest element in the matrix.

Example 1:  Input:  N = 4,  mat[][] = {{16, 28, 60, 64},    K = 3
                                      {22, 41, 63, 91},
                                      {27, 50, 87, 93},
                                     {36, 78, 87, 94 }}
            Output: 27

Expected Time Complexity: O(K*Log(N))
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 50
1 <= mat[][] <= 10000
1 <= K <= N*N
"""

import heapq
from itertools import chain

def kthSmallest(mat, n, k):
    # turn matrix into list [16,28,60,64,22,41,63,91,27,50,87,93,36,78,87,94]
    h = list(chain(*mat))
    # turn list to heapq - priority queue increasing order -> [16,22,36,27,28,41,63,91,64,50,87,93,60,78,87,94]
    heapq.heapify(h)
    # list comprehension to pop k-1 lower values from the h
    [heapq.heappop(h) for i in range(k-1)]
    #return h[0] which is kth small element
    return h[0]