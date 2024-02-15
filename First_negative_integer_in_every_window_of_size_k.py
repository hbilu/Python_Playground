"""
Given an array A[] of size N and a positive integer K,
find the first negative integer for each and every window(contiguous subarray) of size K.

Example:    Input : N = 5, A[] = {-8, 2, 3, -6, 10}, K = 2
            Output : -8 0 -6 -6
            Explanation : First negative integer for each window of size k
                          {-8, 2} = -8
                          {2, 3} = 0 (does not contain a negative integer)
                          {3, -6} = -6
                          {-6, 10} = -6

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(K)

Constraints:
1 <= N <= 105
-105 <= A[i] <= 105
1 <= K <= N
"""

def printFirstNegativeInteger( A, N, K):
    q = []
    result = []
    for i in range(N):
        if q and q[0]<=i-K:
            q.pop(0)
        if A[i] < 0:
            q.append(i)
        if q and i >= K - 1:
            if A[q[0]] < 0:
                result.append(A[q[0]])
        elif not q and i >= K - 1:
            result.append(0)
    return result