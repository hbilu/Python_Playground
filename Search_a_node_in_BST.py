"""
Given a Binary Search Tree and a node value X, find if the node with value X is present in the BST or not.

Example:
Input:         2                X = 87              Output: 1
                \
                 81
               /    \
             42      87
              \       \
               66      90
              /
            45

Expected Time Complexity: O(Height of the BST)
Expected Auxiliary Space: O(1).

Constraints:
1 <= Number of nodes <= 105
"""

class BST:
    def search(self, node, x):
        while node:
            if node.data==x:
                return True
            elif node.data>x:
                node=node.left
            elif node.data<x:
                node=node.right
        return False