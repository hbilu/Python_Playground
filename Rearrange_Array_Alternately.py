"""
Given a sorted array of positive integers.
Your task is to rearrange the array elements alternatively i.e first element should be max value,
second should be min value, third should be second max, fourth should be second min and so on.
Note: Modify the original array itself. Do it without using any extra space. You do not have to return anything.

Example:    Input:  n = 6, arr[] = {1,2,3,4,5,6}    Output: 6 1 5 2 4 3

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= n <= 10^6
1 <= arr[i] <= 10^7
"""


# by using extra space
class Solution:
    def rearrange(self,arr, n):
        result = []
        index=0
        end = n-1
        while(index<=n-1):
            result.append(arr[end])
            result.append(arr[index])
            end -= 1
            index += 1
        for i in range(n):
            arr[i]=result[i]