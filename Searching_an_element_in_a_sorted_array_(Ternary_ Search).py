"""
Given a sorted array arr[] of size N and an integer K.
The task is to check if K is present in the array or not using ternary search.
Returns 1 if K is present in the array, else it returns -1

Example:    Input: N = 5, K = 6, arr[] = {1,2,3,4,6}
            Output: 1

Expected Time Complexity: O(Log3N)
Expected Auxiliary Space: O(1)

Constraints:
1 < N < 106
1 < K < 106
1 < arr[i] < 106
"""

# iterative approach - O(log3N)
class Solution:
    def ternarySearch(self,arr,N,K):
        start = 0
        end = N-1
        while (start<=end):
            middle1 = int(start+(end-start)/3)
            middle2 = int(end-(end-start)/3)
            if arr[middle1]==K:
                return 1
            elif arr[middle2]==K:
                return 1
            elif arr[middle1]>K:
                end = middle1-1
            elif arr[middle2]<K:
                start = middle2+1
            else:
                start = middle1+1
                end = middle2-1
        return -1
