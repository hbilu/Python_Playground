"""
Given an integer array arr of size n. For each element in the array,
check whether the right adjacent element (on the next immediate position) of the array is smaller.
If next element is smaller, update the current index to that element. If not, then  -1.

Note : You need to make changes in the array itself.

Examples:   Input: n = 5, arr[] = {4, 2, 1, 5, 3}
            Output: 2 1 -1 3 -1
            Explanation:    Array elements are 4, 2, 1, 5, 3. Next to 4 is 2 which is smaller,
                            so we print 2. Next of 2 is 1 which is smaller,so we print 1.
                            Next of 1 is 5 which is greater, so we print -1.
                            Next of 5 is 3 which is smaller, so we print 3.
                            Note that for last element, output is always  going to be -1
                            because there is no element on right.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 107
1 ≤ arr[i] ≤ 105
"""

class Solution:
	def immediateSmaller(self,arr,n):
		for index in range(0, n-1):
		    if arr[index]>arr[index+1]:
		        arr[index] = arr[index+1]
		    else:
		        arr[index] = -1
		arr[-1] = -1
		return arr

# ------- Driver code of geekforgeeks -----------
if __name__ == '__main__':
    tcs=int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob = Solution()
        ob.immediateSmaller(arr,n)
        for x in arr:
            print(x, end=" ")
        print()