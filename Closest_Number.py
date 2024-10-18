"""
Given  two integers N and M. The problem is to find the number closest to N and divisible by M.
If there are more than one such number, then output the one having maximum absolute value.

Example 1:  Input:  N = 13 , M = 4
            Output: 12
            Explanation: 12 is the Closest Number to 13 which is divisible by 4.

            Input:  N = -15 , M = 6
            Output: -18
            Explanation: -12 and -18 are both similarly close to -15 and divisible by 6. but -18 has
                         the maximum absolute value. So, Output is -18

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
"""

class Solution:
    def closestNumber(self, N , M):
        n = abs(N)
        m = abs(M)
        remainder = n % m
        if (m-remainder) > remainder:
            answer = n - remainder
        else:
            answer = n + m - remainder
        return - answer if N<0 else answer

# ------- Driver code of geekforgeeks -----------
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = map(int, input().split())
        ob = Solution()
        print(ob.closestNumber(N, M))