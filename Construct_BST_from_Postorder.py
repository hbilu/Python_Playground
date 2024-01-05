"""
Given postorder traversal of a Binary Search Tree, you need to construct a BST from postorder traversal.
The output will be inorder traversal of the constructed BST.

Example 1:
Input:              Output:             Explanation:
6                                       Testcase 1: The BST for the given post order traversal is:
1 7 5 50 40 10      1 5 7 10 40 50      Thus the inorder traversal of BST is: 1 5 7 10 40 50.

Expected Time Complexity: O(No. of  nodes in BST)
Expected Auxiliary Space: O(No. of  nodes in BST)

Constraints:
1 <= T <= 100
1 <= N <= 200
"""

class Solution:
    def constructTree(self, post, n):
        post.sort()
        return self.helper(post)

    def helper(self, arr):
        if not arr:
            return
        mid = (len(arr)) // 2
        root = Node(arr[mid])
        root.left = self.helper(arr[:mid])
        root.right = self.helper(arr[mid + 1:])
        return root