"""
Third largest element
Given an array, arr of positive integers.
Find the third largest element in it. Return -1 if the third largest element is not found.

Examples:   Input: arr[] = [2, 4, 1, 3, 5]
            Output: 3

Expected Time Complexity: O(n)
Expected Space Complexity: O(1)

Constraints:
1 ≤ arr.size ≤ 105
1 ≤ arr[i] ≤ 105
"""

class Solution:
    def thirdLargest(self,arr):
        if len(arr)<3:
            return -1
        arr.sort()
        return arr[-3]

# ------- Driver code of geekforgeeks -----------
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr))