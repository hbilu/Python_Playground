"""
Given a sorted array. Convert it into a Height balanced Binary Search Tree (BST).
If there exist many such balanced BST consider the tree whose preorder is lexicographically smallest.

Example:    Input: nums = {1, 2, 3, 4}
            Output: {2, 1, 3, 4}
            Explanation: The preorder traversal of the following BST formed is {2, 1, 3, 4}:
                              2
                            /   \
                           1     3
                                  \
                                   4

Your Task:
Your task is to complete the function sortedArrayToBST() which takes the sorted array nums as input paramater
and returns the preorder traversal of height balanced BST.
If there exist many such balanced BST consider the tree whose preorder is lexicographically smallest.

Expected Time Complexity: O(n)
Expected Space Complexity: O(n)

Constraints:
1 ≤ |nums| ≤ 104
-104 ≤ nums[i] ≤ 104
"""


class Solution:
    def BST(self, arr, res, low, high):
        if low > high:
            return
        middle = (low + high) // 2
        res.append(arr[middle])
        self.BST(arr, res, low, middle - 1)
        self.BST(arr, res, middle + 1, high)

    def sortedArrayToBST(self, nums):
        res = []
        self.BST(nums, res, 0, len(nums) - 1)
        return res