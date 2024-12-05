
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
"""
 Updates on the problem: 
 - If multiple occurrences are there, please return the smallest index.
 - Try to solve this problem in constant space i.e O(1)
"""
# updated solution:
class Solution:
    def binarysearch(self, arr, k):
        n = len(arr)
        left = 0
        right = n-1
        index = -1
        while left<=right:
            mid = (left+right)//2
            if arr[mid] == k:
                index = mid
                right = mid-1
            elif arr[mid]>k:
                right = mid-1
            else: # arr[mid] > k
                left = mid+1
        return index

# ------- Driver code of geekforgeeks -----------
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)
        print("~")