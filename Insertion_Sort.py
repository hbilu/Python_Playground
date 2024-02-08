"""
The task is to complete the insert() function which is used to implement Insertion Sort.

Example:    Input: N = 10, arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
            Output: 1 2 3 4 5 6 7 8 9 10

Expected Time Complexity: O(N*N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 1000
1 <= arr[i] <= 1000
"""

class Solution:
    def insert(self, alist, index, n):
        pass

    def insertionSort(self, alist, n):
        for i in range(1, n):
            key = alist[i]
            j = i - 1
            while j >= 0 and key < alist[j]:
                alist[j + 1] = alist[j]
                j -= 1
            alist[j + 1] = key