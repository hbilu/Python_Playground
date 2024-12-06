"""
Given an array arr[] of integers, determine whether it contains a triplet whose sum equals zero.
Return true if such a triplet exists, otherwise, return false.

Examples:   Input: arr[] = [0, -1, 2, -3, 1]
            Output: true
            Explanation: The triplet [0, -1, 1] has a sum equal to zero.

            Input: arr[] = [1, 2, 3]
            Output: false
            Explanation: No triplet with a sum of zero exists.

Constraints:
1 <= arr.size() <= 103
-106 <= arr[i] <= 106

"""
# first way: O(n^2) time complexity
class Solution:
    def findTriplets(self, arr):
        arr.sort()
        n = len(arr)
        for i in range(n-2):
            left = i+1
            right = n-1
            while left<right:
                triple_sum = arr[i]+arr[left]+arr[right]
                if triple_sum == 0:
                    return True
                elif triple_sum < 0:
                    left += 1
                else:
                    right -= 1
        return False

# second way: O(n^2) time complexity
class Solution:
    def findTriplets(self, arr):
        n = len(arr)
        pair_sum_map = {}
        for i in range(n):
            for j in range(i+1, n):
                pair_sum = arr[i]+arr[j]
                if pair_sum not in pair_sum_map:
                    pair_sum_map[pair_sum] = []
                pair_sum_map[pair_sum].append((i, j))
        for pair_sum, pairs in pair_sum_map.items():
            diff = 0 - pair_sum
            for i in range(n):
                if arr[i] == diff:
                    for pair in pairs:
                        if i!=pair[0] and i!=pair[1]:
                            return True
        return False

# ------- Driver code of geekforgeeks -----------
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    n = len(arr)  # get the length of the array
    if Solution().findTriplets(arr):
        print("true")
    else:
        print("false")