"""
Given an array of integers in[] representing inorder traversal of elements of a binary tree.
Return true if the given inorder traversal can be of a valid Binary Search Tree.

Example:    Input: in = [8, 14, 45, 64, 100]
            Output: True

Expected Time Complexity: O(n)
Expected Space Complexity: O(1)

Constraints:
1<=n<=105
1<=in[i]<=109
"""

class Solution:
    def isBSTTraversal(self, nums):
        for i in range(1,len(nums)):
            if nums[i-1]>=nums[i]:
                return False
        return True