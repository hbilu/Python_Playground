"""
Given an array arr[] containing integers and an integer k,
your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k.
It is guaranteed that a valid subarray exists.

Examples:

    Input: arr[] = [10, 5, 2, 7, 1, 9], k = 15
    Output: 4
    Explanation: The subarray [5, 2, 7, 1] has a sum of 15 and length 4.

    Input: arr[] = [-1, 2, -3], k = -2
    Output: 3
    Explanation: The subarray [-1, 2, -3] has a sum of -2 and length 3.

    Input: arr[] = [1, -1, 5, -2, 3], k = 3
    Output: 4
    Explanation: The subarray [1, -1, 5, -2] has a sum of 3 and a length 4.

Constraints:
1 ≤ arr.size() ≤ 106
-109 ≤ arr[i], k ≤ 109

"""

class Solution:
    def lenOfLongestSubarr(self, arr, k):
        prefix_sum = {}
        current_sum = 0
        max_length = 0
        for i, num in enumerate(arr):
            current_sum += num
            if current_sum == k:
                max_length = max(max_length, i+1)
            if current_sum - k in prefix_sum:
                max_length = max(max_length, i - prefix_sum[current_sum-k])
            if current_sum not in prefix_sum:
                prefix_sum[current_sum] = i
        return max_length

# ------- Driver code of geekforgeeks -----------
if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.lenOfLongestSubarr(arr, k))
        tc -= 1
        print("~")