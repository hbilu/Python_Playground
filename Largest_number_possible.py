"""
Given two numbers 'N' and 'S' , find the largest number that can be formed
with 'N' digits and whose sum of digits should be equals to 'S'. Return -1 if it is not possible.

Example:    Input: N = 2, S = 9
            Output: 90
            Explaination: It is the biggest number with sum of digits equals to 9.

Expected Time Complexity: O(N)
Exepcted Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 104
0 ≤ S ≤ 105
"""


class Solution:
    def findLargest(self, N, S):
        limit = 9 * N
        if (S == 0 and N > 1) or limit < S:
            return -1
        elif S == 0 and N == 1:
            return 0
        ans = ""
        while S != 0:
            if 9 <= S:
                ans += "9"
                S -= 9
            else:
                ans += str(S)
                S -= S
        if len(ans) == N:
            return int(ans)
        else:
            ans += "0" * (N - len(ans))
        return int(ans)