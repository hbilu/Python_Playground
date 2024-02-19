"""
Given two arrays of integers A[] and B[] of size N and M, the task is to check if a pair of values
(one value from each array) exists such that swapping the elements of the pair will make the sum of two arrays equal.

Example:    Input: N = 6, M = 4, A[] = {4, 1, 2, 1, 1, 2}, B[] = (3, 6, 3, 3)
            Output: 1
            Explanation: Sum of elements in A[] = 11 Sum of elements in B[] = 15,
                         To get same sum from both arrays, we can swap following values: 1 from A[] and 3 from B[]

Expected Time Complexity: O(MlogM+NlogN).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N, M ≤ 106
"""
# O(n+2m) -> O(n+m)
class Solution:
    def findSwapValues(self,a, n, b, m):
        #suma-ax+bx = sumb-bx+ax
        #2bx-2ax = sumb-suma
        # bx-ax = (sumb-suma)/2
        suma = sum(a)   # O(n) complexity
        sumb = sum(b)   # O(m) comlexity
        if sumb>suma:
            a, b = b, a
            suma, sumb = sumb, suma
        if (suma-sumb)%2!=0:
            return -1
        diff = (sumb-suma)//2
        setA = set(a)
        for bx in b: # 0(m) complexity
            ax = bx-diff
            if ax in setA: # 0(1) to lookup in set because hash-based lookup
                return 1
        return -1