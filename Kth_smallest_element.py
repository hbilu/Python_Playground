"""
Given an array arr[] and an integer K where K is smaller than size of array,
the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.
Note :-  l and r denotes the starting and ending index of the array.

Example:    Input: N = 6, arr[] = 7 10 4 3 20 15, K = 3, L=0 R=5
            Output : 7
            Explanation : 3rd smallest element in the given array is 7.

Expected Time Complexity: O(n*log(n) )
Expected Auxiliary Space: O(log(n))
Constraints:
1 <= N <= 105
 L==0
 R==N-1
1<= arr[i] <= 105
1 <= K <= N
"""

class Solution:
    def kthSmallest(self,arr, l, r, k):
        sorted_arr=sorted(arr) #python sorted() has O(NlogN) complexity
        return sorted_arr[k-1]