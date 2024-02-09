
"""
Check for BST (Binary Search Tree)

Given the root of a binary tree. Check whether it is a BST or not.
Note: We are considering that BSTs can not contain duplicate Nodes.

A BST is defined as follows:
-> The left subtree of a node contains only nodes with keys less than the node's key.
-> The right subtree of a node contains only nodes with keys greater than the node's key.
-> Both the left and right subtrees must also be binary search trees.

The Task:
The task is to complete the function isBST() which takes the root of the tree as a parameter
and returns true if the given binary tree is BST, else returns false.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the BST).

"""
# first way
class Solution:

    def checkBST(self, root, MIN, MAX):
        if root == None:
            return 1
        if root.data < MIN or root.data > MAX:
            return 0
        return self.checkBST(root.left, MIN, root.data - 1) and self.checkBST(root.right, root.data + 1, MAX)

    def isBST(self, root):
        INT_MAX = 4294967296
        INT_MIN = -4294967296
        return self.checkBST(root, INT_MIN, INT_MAX)


# second way: if InOrder traversal of BST is sorted, it is BST
class Solution:
    def isBST(self, root):
        stack = []
        arr = []
        if root==None:
            return
        current = root
        while (True):
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                arr.append(current.data)
                current = current.right
            else:
                break
        for i in range(1,len(arr)):
            if arr[i]<=arr[i-1]:
                return False
        return True
