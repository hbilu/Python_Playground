"""
Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.

Example:    Input: N = 10, arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
            Output: 1 2 3 4 5 6 7 8 9 10

Your Task:
Complete the functions select() and selectionSort() ,
where select() takes arr[] and starting point of unsorted array i as input parameters and
returns the selected element for each iteration in selection sort,
and selectionSort() takes the array and it's size and sorts the array.

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 10^3

"""

# first - selection sort
class Solution:

    def select(self, arr, i):
        pass

    def selectionSort(self, arr, n):
        for i in range(n):
            small = i
            for j in range(i + 1, n):
                if arr[j] < arr[small]:
                    small = j
            if small != i:
                arr[i], arr[small] = arr[small], arr[i]

# second
class Solution:

    def select(self, arr, i):
        pass

    def selectionSort(self, arr, n):
        for i in range(n):
            for j in range(i + 1, n):
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]