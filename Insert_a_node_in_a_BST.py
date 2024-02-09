"""
Given a BST and a key K. If K is not present in the BST,
Insert a new Node with a value equal to K into the BST. If K is already present in the BST, don't modify the BST.

Example:
    Input:  K = 4,          Output: 1 2 3 4 6
             2
           /   \
          1     3
                 \
                  6

    Explanation:  After inserting the node 4 Inorder traversal of the above tree will be 1 2 3 4 6.

Expected Time Complexity: O(Height of the BST).
Expected Auxiliary Space: O(Height of the BST).

Constraints:
1 <= Number of nodes initially in BST <= 105
1 <= K <= 109
"""
class Solution:
    def insert(self,root, Key):
        if root == None:
            return Node(Key)
        elif root.data == Key:
            return root
        elif Key>root.data:
            root.right = self.insert(root.right,Key)
        elif Key<root.data:
            root.left = self.insert(root.left,Key)
        return root