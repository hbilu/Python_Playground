"""
Given an array arr consisting of only 0's and 1's in random order.
Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.

Examples :  Input: arr[] = [0, 0, 1, 1, 0]
            Output: [0, 0, 0, 1, 1]
            Explanation:  After segregation, all the 0's are on the left and 1's are on the right.
                          Modified array will be [0, 0, 0, 1, 1].

            Input: arr[] = [1, 1, 1, 1]
            Output: [1, 1, 1, 1]
            Explanation: There are no 0s in the given array, so the modified array is [1, 1, 1, 1]

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 1
"""

class Solution:
    def segregate0and1(self, arr):
        left = 0
        right = len(arr)-1
        while left<=right:
            if arr[left]==0:
                left += 1
            elif arr[left]==1:
                arr[right], arr[left] = arr[left], arr[right]
                right -= 1

# ------- Driver code of geekforgeeks -----------
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr
    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()