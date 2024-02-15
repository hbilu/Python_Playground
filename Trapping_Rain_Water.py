"""
Given an array arr[] of N non-negative integers representing the height of blocks.
If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season.

Example:    Input: N = 4, arr[] = {7,4,0,9}
            Output: 10
            Explanation: Water trapped by above block of height 4 is 3 units and above
                         block of height 0 is 7 units. So, the total unit of water trapped is 10 units.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
3 < N < 106
0 < Ai < 108
"""

class Solution:
    def trappingWater(self, arr, n):
        pool = 0
        left = [0] * n
        right = [0] * n
        left[0] = arr[0]
        right[n - 1] = arr[n - 1]
        for i in range(1, n):
            left[i] = max(left[i - 1], arr[i])
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], arr[i])
        for i in range(1, n - 1):
            capacity = min(left[i - 1], right[i + 1])
            if arr[i] < capacity:
                pool += capacity - arr[i]
        return pool
