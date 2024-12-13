"""
Given an array of positive integers arr[], return the second largest element from the array.
If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:   Input: arr[] = [12, 35, 1, 10, 34, 1]
            Output: 34
            Explanation: The largest element of the array is 35 and the second largest element is 34.

            Input: arr[] = [10, 10, 10]
            Output: -1
            Explanation: The largest element of the array is 10 and the second largest element does not exist.

Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105
"""
# time complexity O(n)
class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1
        first, second = float('-inf'), float('-inf')
        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second and num < first:
                second = num
        return second if second != float('-inf') else -1

# time complexity O(nlogn)
class Solution:
    def getSecondLargest(self, arr):
        x = sorted(set(arr), reverse=True)
        if len(x) >= 2:
            return x[1]
        else:
            return -1

# ------- Driver code of geekforgeeks -----------
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")