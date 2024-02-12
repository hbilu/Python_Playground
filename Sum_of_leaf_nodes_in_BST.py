"""
Given a Binary Search Tree with n nodes, find the sum of all leaf nodes.
BST has the following property (duplicate nodes are possible):

Example 1:
Input:
n = 6
arr = {67, 34, 82, 12, 45, 78}
Output:
135
Explanation:
In first test case, the BST for the given input will be-
                67
             /     \
           34       82
          /   \    /
         12   45  78

Hence, the required sum= 12 + 45 + 78 = 135

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= n <= 104
1 <= Value of each node <= 105
"""

class Solution:
    def sumOfLeafNodes(self, root):
        if not root:
            return 0
        if root.left is None and root.right is None:
            return root.data
        left_sum = self.sumOfLeafNodes(root.left)
        right_sum = self.sumOfLeafNodes(root.right)
        return left_sum + right_sum