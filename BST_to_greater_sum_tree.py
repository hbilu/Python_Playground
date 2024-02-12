"""
Given a BST with unique node values, transform it into greater sum tree where each node contains sum of all nodes greater than that node.

Example:
Input:
           2
         /    \
        1      6
              /  \
             3    7
Output: 18 16 13 7 0
Explanation:
Every node is replaced with the
sum of nodes greater than itself.
The resultant tree is:
               16
             /    \
           18       7
                  /   \
                 13    0

Expected Time Complexity: O(N), N = number of nodes
Expected Auxiliary Space: O(N), N = number of nodes

Constraints :
1 ≤ N ≤ 104
"""

class Solution:
    def transformTree(self, root):
        running_sum = [0]
        def reverse_inorder(node):
            if not node:
                return
            reverse_inorder(node.right)
            original_data = node.data
            node.data = running_sum[0]
            running_sum[0] += original_data
            reverse_inorder(node.left)
        reverse_inorder(root)
        return root