"""
Given an array arr, rotate the array by one position in clock-wise direction.

Examples:       Input: arr = [1, 2, 3, 4, 5]
                Output: [5, 1, 2, 3, 4]
                Explanation: If we rotate arr by one position in clockwise 5 come to the front and
                             remaining those are shifted to the end.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1<=arr.size()<=105
0<=arr[i]<=105
"""
# first
class Solution:
    def rotate(self, arr):
        arr[:]=arr[len(arr)-1:]+arr[:len(arr)-1]
        return arr

# second
class Solution:
    def rotate(self, arr):
        for i in range(len(arr)-1):
            arr.append(arr.pop(0))
        return arr

# ------- Driver code of geekforgeeks -----------
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.rotate(arr)
        print(" ".join(map(str, arr)))
        t -= 1