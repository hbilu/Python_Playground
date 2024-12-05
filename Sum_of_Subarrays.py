"""
Given an array arr. Find the sum of all subarrays of the array since the sum could be very large print the sum modulo (109+7).

Examples:   Input: arr[] = [1, 2, 3]
            Output: 20
            Explanation: All subarray sums are: [1] = 1, [2] = 2, [3] = 3, [1,2] = 3, [2,3] = 5, [1,2,3] = 6.
                         Thus total sum is 1+2+3+3+5+6 = 20.

Explanation: All subarray sums are: [1] = 1 [3] = 3 [1,3] = 4. Thus total sum is 1+3+4 = 8.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints :
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 109
"""

class Solution:
    def subarraySum(self, arr):
        MOD = 10 ** 9 + 7
        n = len(arr)
        total_sum = 0
        for i in range(n):
            # The number of subarrays that include element arr[i] is (𝑖+1)×(𝑛−𝑖)
            # (i+1) —> Number of ways to pick the starting index of the subarray
            # (n−i) —> Number of ways to pick the ending index of the subarray
            # Calculate the contribution of arr[i] to the total sum
            contribution = arr[i] * (i + 1) * (n - i)
            total_sum = (total_sum + contribution) % MOD
        return total_sum

# ------- Driver code of geekforgeeks -----------
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.subarraySum(arr)
        print(res)
        # print("~")
        t -= 1
        print("~")