"""
Given an integer array of N elements. You need to find the maximum sum of two elements such that sum is closest to zero.

Example 1:  Input:  N = 3 arr[] = {-8 -66 -60}
            Output: -68
            Explanation: Sum of two elements closest to zero is -68 using numbers -60 and -8.
Example 2:  Input: N = 6 arr[] = {-21 -67 -37 -18 4 -65}
            Output: -14
            Explanation: Sum of two elements closest to zero is -14 using numbers -18 and 4.
Note : In Case if we have two of more ways to form sum of two elements closest to zero return the maximum sum.

Expected Time Complexity: O(N*logN).
Expected Auxiliary Space: O(1).

Constraints:
2 ≤ N ≤ 5 * 105
-106 ≤ arr[i] ≤ 106
"""

class Solution:
    def closestToZero(self, arr, n):
        arr.sort()
        closest_sum = float('inf')
        max_closest_sum = -float('inf')
        left = 0
        right = n - 1
        while left < right:
            curr_sum = arr[left] + arr[right]
            if abs(curr_sum) < abs(closest_sum):
                closest_sum = curr_sum
                max_closest_sum = curr_sum
            elif abs(curr_sum) == abs(closest_sum):
                # If the absolute values are the same, take the maximum sum
                max_closest_sum = max(max_closest_sum, curr_sum)
            if curr_sum < 0:
                left += 1
            else:
                right -= 1
        return max_closest_sum

# ------- Driver code of geekforgeeks -----------
t = int (input ())
for tc in range(t):
    n = int (input ())
    arr = list(map(int, input().split()))
    ob = Solution()
    print (ob.closestToZero (arr, n))
    print("~")