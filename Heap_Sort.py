"""
Heap Sort
Given an array of size N. T
he task is to sort the array elements by completing functions heapify() and buildHeap()
which are used to implement Heap Sort.

Example:    Input: N = 5, arr[] = {4,1,3,9,7}
            Output: 1 3 4 7 9
            Explanation: After sorting elements using heap sort, elements will be in order as 1,3,4,7,9.

Expected Time Complexity: O(N * Log(N)).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 106
1 ≤ arr[i] ≤ 106
"""
class Solution:
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def buildHeap(self, arr, n):
        for i in range(int((n - 2) / 2), -1, -1):
            self.heapify(arr, n, i)

    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
