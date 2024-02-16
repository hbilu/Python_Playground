"""
Given an array arr[] of size N and an integer K. Find the maximum for each and every contiguous subarray of size K.

Example:    Input:  N = 9, K = 3, arr[] = 1 2 3 1 4 5 2 3 6
            Output: 3 3 4 5 5 5 6
            Explanation: 1st contiguous subarray = {1 2 3} Max = 3
                         2nd contiguous subarray = {2 3 1} Max = 3
                         3rd contiguous subarray = {3 1 4} Max = 4
                         4th contiguous subarray = {1 4 5} Max = 5
                         5th contiguous subarray = {4 5 2} Max = 5
                         6th contiguous subarray = {5 2 3} Max = 5
                         7th contiguous subarray = {2 3 6} Max = 6

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(k)

Constraints:
1 ≤ N ≤ 105
1 ≤ K ≤ N
0 ≤ arr[i] ≤ 107
"""

# 0(N*K) complexity
class Solution:
    def max_of_subarrays(self, arr, n, k):
        answer = []
        for i in range(0, n - (k - 1), 1):
            answer.append(max(arr[i:i + k]))
        return answer

# 0(N) complexity with list []
class Solution:
    def max_of_subarrays(self,arr,n,k):
        q = []
        answer = []
        for i in range(k):
            while q and arr[i]>=arr[q[-1]]:
                q.pop()
            q.append(i),
        for i in range(k, n):
            answer.append(arr[q[0]])
            while q and q[0] <= i-k:
                q.pop(0) #pop(0) is O(N)
            while q and arr[i]>=arr[q[-1]]:
                q.pop()
            q.append(i)
        answer.append(arr[q[0]])
        return answer

# 0(N) with deque
class Solution:
    def max_of_subarrays(self,arr,n,k):
        q = deque()
        answer = []
        for i in range(k):
            while q and arr[i]>=arr[q[-1]]:
                q.pop()
            q.append(i),
        for i in range(k, n):
            answer.append(arr[q[0]])
            while q and q[0] <= i-k:
                q.popleft()
            while q and arr[i]>=arr[q[-1]]:
                q.pop()
            q.append(i)
        answer.append(arr[q[0]])
        return answer