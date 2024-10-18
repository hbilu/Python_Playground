"""
Given a sorted array arr[] of size n without duplicates, and given a value x.
Floor of x is defined as the largest element k in arr[] such that k is smaller than or equal to x.
Find the index of k(0-based indexing).

Examples    Input: n = 7, x = 0 arr[] = {1,2,8,10,11,12,19}
            Output: -1
            Explanation: No element less than 0 is found. So output is "-1".

            Input: n = 7, x = 5 arr[] = {1,2,8,10,11,12,19}
            Output: 1
            Explanation: Largest Number less than 5 is 2 (i.e k = 2), whose index is 1(0-based indexing).

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ n ≤ 107
1 ≤ arr[i] ≤ 1018
0 ≤ x ≤ arr[n-1]
"""

# using Binary Search - 0(logN) - expected time complexity
class Solution:
    def findFloor(self,A,N,X):
        low = 0
        high = N
        ans = -1
        while low<high:
            mid = (low+high)//2
            if A[mid]<=X:
                ans = mid
                low = mid+1
            else:
                high = mid
        return ans

# O(n)
class Solution:
    def findFloor(self,A,N,X):
        floor = 0
        for i in range(N):
            if A[i]<X:
                floor = A[i]
        for i in range(N):
            if A[i]==floor:
                return i
        return -1

# ------- Driver code of geekforgeeks -----------
import math

def main():
    T = int(input())
    while (T > 0):
        NX = [int(x) for x in input().strip().split()]
        N = NX[0]
        X = NX[1]
        A = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.findFloor(A, N, X))
        T -= 1

if __name__ == "__main__":
    main()
