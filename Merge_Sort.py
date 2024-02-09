"""
Given an array arr[], its starting position l and its ending position r. Sort the array using merge sort algorithm.

Example:    Input: N = 5, arr[] = {4 1 3 9 7}
            Output: 1 3 4 7 9

Your task is to complete the function merge() which takes arr[], l, m, r as its input parameters
and modifies arr[] in-place such that it is sorted from position l to position r, and function mergeSort()
which uses merge() to sort the array in ascending order using merge sort algorithm.

Expected Time Complexity: O(nlogn)
Expected Auxiliary Space: O(n)

Constraints:
1 <= N <= 105
1 <= arr[i] <= 105
"""

# first

class Solution:
    def merge(self,arr, l, m, r):
        pass
    def mergeSort(self, arr, l, r):
        if len(arr) > 1:
            middle = int((l + r) / 2)
            L = arr[:middle]
            R = arr[middle:]
            self.mergeSort(L, 0, len(L))
            self.mergeSort(R, 0, len(R))
            arr.clear()
            while len(L) > 0 and len(R) > 0:
                if L[0] < R[0]:
                    arr.append(L.pop(0))
                elif R[0] < L[0]:
                    arr.append(R.pop(0))
            for i in L:
                arr.append(i)
            for i in R:
                arr.append(i)

# second
    def mergeSort(self, arr, l, r):
        if len(arr) > 1:
            middle = int((l + r) / 2)
            L = arr[:middle]
            R = arr[middle:]
            self.mergeSort(L, 0, len(L))
            self.mergeSort(R, 0, len(R))
            ak = lk = rk = 0
            while lk < len(L) and rk < len(R):
                if L[lk] < R[rk]:
                    arr[ak] = L[lk]
                    lk += 1
                elif R[rk] < L[lk]:
                    arr[ak] = R[rk]
                    rk += 1
                ak += 1
            while lk < len(L):
                arr[ak] = L[lk]
                lk += 1
                ak += 1
            while rk < len(R):
                arr[ak] = R[rk]
                rk += 1
                ak += 1


