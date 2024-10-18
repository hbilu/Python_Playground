"""
Given an array arr of positive integers. Reverse every sub-array group of size k.

Note: If at any instance, k is greater or equal to the array size, then reverse the entire array.
You shouldn't return any array, modify the given array in place.

Examples:
Input: k = 3, arr= [1, 2, 3, 4, 5]
Output: [3, 2, 1, 5, 4]
Explanation: First group consists of elements 1, 2, 3. Second group consists of 4,5.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ arr.size(), k ≤ 107
1 ≤ arr[i] ≤ 1018
"""

# first way
class Solution:
    def reverseInGroups(self, arr, k):
        for i in range(0, len(arr), k):
            temp = arr[i:i+k]
            arr[i:i+k] = reversed(temp)

# second way
class Solution:
    def reverseInGroups(self, arr, k):
        index = 0
        while (index < len(arr)):
            left = index
            right = min(index+k-1, len(arr-1)
            while (left < right):
                arr[left], arr[right] = arr[right], arr[left]
                left = left + 1
                right = right - 1
            index = index + k

# ------- Driver code of geekforgeeks -----------
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    line_index = 1
    for _ in range(t):
        k = int(data[line_index])
        line_index += 1
        arr = list(map(int, data[line_index].split()))
        line_index += 1
        ob = Solution()
        obreverseInGroups(arr, k)
        print(" ".join(map(str, arr)))