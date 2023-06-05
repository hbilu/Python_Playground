
"""
Binary Search

Given a sorted array of size N and an integer K,
find the position at which K is present in the array using binary search.

The task:
Complete the function binarysearch() which takes arr[], N and K as input parameters
and returns the index of K in the array. If K is not present in the array, return -1.

Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(LogN) if solving recursively and O(1) otherwise.

"""

class Solution:
	def binarysearch(self, arr, n, k):
	    low=0
	    high=n-1
	    while low<=high:
	        middle=int((low+high)/2)
	        if arr[middle]==k:
	            return middle
	        elif k<arr[middle]:
	            high=middle-1
	        elif k>arr[middle]:
	            low=middle+1
        return -1
