"""
You are given two arrays, A and B, of equal size N.
The task is to find the minimum value of A[0] * B[0] + A[1] * B[1] + .... + A[N-1] * B[N-1],
where shuffling of elements of arrays A and B is allowed.

Example:
 Input: N = 5 - A[] = {6, 1, 9, 5, 4} - B[] = {3, 4, 8, 2, 4}
 Output: 80
 Explanation:  2*9+3*6+4*5+4*4+8*1 = 80

Expected Time Complexity: O(N. log(N))
Expected Auxiliary Space: O(1)

"""

def minValue(self, a, b, n):
    a.sort()
    b.sort(reverse=True)
    msum = 0
    for index in range(0, n, 1):
        msum += a[index] * b[index]
    return msum