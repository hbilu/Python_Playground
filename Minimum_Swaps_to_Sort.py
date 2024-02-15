"""
Given an array of n distinct elements.
Find the minimum number of swaps required to sort the array in strictly increasing order.
If the array is already sorted, return 0.

Example:    Input:  nums = {2, 8, 5, 4}
            Output: 1
            Explanation: swap 8 with 4.

Expected Time Complexity: O(nlogn)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ n ≤ 105
1 ≤ numsi ≤ 106
"""

from collections import OrderedDict

class Solution:

    def minSwaps(self, nums):
        odic = OrderedDict()

        for i in range(len(nums)):
            odic[nums[i]] = i
        sorted_odic = OrderedDict(sorted(odic.items()))
        swap_count = 0
        for i, (k, v) in enumerate(sorted_odic.items()):
            if i != v:
                nums[i], nums[v] = nums[v], nums[i]
                sorted_odic[nums[i]], sorted_odic[nums[v]] = sorted_odic[nums[v]], sorted_odic[nums[i]]
                swap_count += 1
        return swap_count