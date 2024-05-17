'''
Given an array A of size N of integers.
Return an array that contains 2 elements the first one will be a minimum element
and the second will be a maximum of an array.

Example:    Input: N = 6, A[] = {3, 2, 1, 56, 10000, 167}
            Output: 1 10000
            Explanation: minimum and maximum elements of array are 1 and 10000.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 105
1 <= Ai <=1012
'''

def getMinMax( a, n):
    # Because of having O(N) time complexity, min() and max() are used.
    return [min(a), max(a)]