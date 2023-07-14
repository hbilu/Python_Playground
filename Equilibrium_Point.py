"""
Given an array A of n positive numbers. The task is to find the first Equilibrium Point in an array.
Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

Example:
Input:
 n = 5
 A[] = {1,3,5,2,2}
Output: 3
Explanation:  equilibrium point is at position 3 as elements before it (1+3) = elements after it (2+2).

Return -1 if no such point exists.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

"""


def equilibriumPoint(self, A, N):
    if N == 1:
        return 1
    if N == 2:
        return -1
    s = 0
    e = N - 1
    lsum = A[s]
    rsum = A[e]
    while s < N - 2 and e >= 1 and e > s:
        if lsum == rsum:
            if s+1 == e-1:
                # +1 for index of the equilibrium point -> s+1
                # and +1 for its position
                return s + 2
            else:
                e -= 1
                rsum += A[e]
                s += 1
                lsum += A[s]
        if lsum > rsum:
            e -= 1
            rsum += A[e]
        elif lsum < rsum:
            s += 1
            lsum += A[s]
        else:
            return -1
    return -1