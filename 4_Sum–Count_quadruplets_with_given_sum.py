"""
Given an array arr[] and an integer target, you need to find and return the count of quadruplets such that
the index of each element of the quadruplet is unique and the sum of the elements is equal to target.

Example:    Input: arr[] = [4, 5, 3, 1, 2, 4], target = 13
            Output: 3
            Explanation:    Three quadruplets with sum 13 are:
                            arr[0] + arr[2] + arr[4] + arr[5] = 4 + 3 + 2 + 4 = 13
                            arr[0] + arr[1] + arr[2] + arr[3] = 4 + 5 + 3 + 1 = 13
                            arr[1] + arr[2] + arr[3] + arr[5] = 5 + 3 + 1 + 4 = 13

Constraints:
1 <= arr.length <= 103
-105 <=arr[i]<= 105
-105 <=target<= 105
"""


class Solution:
    def countSum(self, arr, target):
        n = len(arr)
        count = 0
        pair_sum_map = {}
        for i in range(n):
            for j in range(i + 1, n):
                pair_sum = arr[i] + arr[j]
                if pair_sum not in pair_sum_map:
                    pair_sum_map[pair_sum] = []
                pair_sum_map[pair_sum].append((i, j))
        seen_quadruplets = set()
        for pair_sum, pairs in pair_sum_map.items():
            diff = target - pair_sum
            if diff in pair_sum_map:
                for (i, j) in pairs:
                    for (k, l) in pair_sum_map[diff]:
                        # Ensure all indices are distinct
                        if i < j < k < l:
                            quadruplet = (i, j, k, l)
                            if quadruplet not in seen_quadruplets:
                                seen_quadruplets.add(quadruplet)
                                count += 1
        return count

# ------- Driver code of geekforgeeks -----------
from collections import defaultdict
if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        arr = list(map(int, input().split()))
        target = int(input())
        obj = Solution()
        print(obj.countSum(arr, target))
        print("~")