"""
Quick Sort is a Divide and Conquer algorithm.
It picks an element as a pivot and partitions the given array around the picked pivot.
Given an array arr[], its starting position is low (the index of the array) and
its ending position is high(the index of the array).
Consider the last element as the pivot such that all the elements less than(or equal to) the pivot lie before it
and the elements greater than it lie after the pivot.

Note: The low and high are inclusive.

Example:    Input: N = 5,   arr[] = { 4, 1, 3, 9, 7}
            Output: 1 3 4 7 9

Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(logN)

Constraints:
1 <= N <= 103
1 <= arr[i] <= 104

"""

# with Lomuto partition - (takes pivot high as expected in the practice)
class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            pivotPos = self.partition(arr, low, high)
            self.quickSort(arr, low, pivotPos - 1)
            self.quickSort(arr, pivotPos + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        pos = low - 1
        for id in range(low, high):
            if arr[id] <= pivot:
                pos += 1
                arr[pos], arr[id] = arr[id], arr[pos]
        arr[pos + 1], arr[high] = arr[high], arr[pos + 1]
        return pos + 1

# with Hoare's partition (pivot is taken as low to exercise)
class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            pivotPos = self.partition(arr, low, high)
            self.quickSort(arr, low, pivotPos - 1)
            self.quickSort(arr, pivotPos + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high
        while (True):
            while (arr[i] < pivot):
                i += 1
            while (arr[j] > pivot):
                j -= 1
            if (i >= j):
                return j
            arr[i], arr[j] = arr[j], arr[i]
