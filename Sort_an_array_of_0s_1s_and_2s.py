"""
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

Your task is to complete the function sort012() that takes an array arr and N as input parameters and sorts the array in-place.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

"""

# first way --> instead of writing a function, python built-in sort() method for the list can be used.
arr.sort()

# second way
def sort012(self, arr, n):
    low = 0
    i = 0
    high = n - 1
    while i <= high:
        if arr[i] == 0:
            arr[low], arr[i] = arr[i], arr[low]
            low += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        # if arr[i] == 2
        else:
            arr[high], arr[i] = arr[i], arr[high]
            high -= 1