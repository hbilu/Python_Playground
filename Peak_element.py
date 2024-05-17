'''
Given an 0-indexed array of integers arr[] of size n, find its peak element and return it's index.
An element is considered to be peak if it's value is greater than or equal to the values of its adjacent elements
(if they exist).
Note: The output will be 1 if the index returned by your function is correct; otherwise, it will be 0.

Example:    Input: n = 7, arr[] = {1, 1, 1, 2, 1, 1, 1}
            Output: 1
            Explanation: In this case there are 5 peak elements with indices as {0,1,3,5,6}.
                         Returning any of them will give you correct answer.
Your Task:
Complete the function peakElement() which takes the array arr[] and its size n as input parameters
and returns the index of the peak element.

Expected Time Complexity: O( log(n) ).
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 105
1 ≤ arr[i] ≤ 106

'''

# Using binary search over indexes to achieve 0(log(n)) time complexity
class Solution:
    def peakElement(self,arr, n):
        left = 0
        right = n-1
        while left<=right:
            middle = (left+right)//2
            # If there is a peak element, return its index.
            if (middle==0 or arr[middle]>=arr[middle-1]) and (middle==n-1 or arr[middle]>=arr[middle+1]):
                    return middle
            # If middle-1 is greater than middle, the peak is on the left side.
            elif middle>0 and arr[middle-1]>arr[middle]:
                right=middle-1
            # Otherwise, the peak is on the right side.
            else:
                left=middle+1
        # If there is no peak element, return 0.
        return 0