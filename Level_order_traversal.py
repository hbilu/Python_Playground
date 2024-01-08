"""
Given a binary tree, find its level order traversal.
Level order traversal of a tree is breadth-first traversal for the tree.
Input:
        10
     /      \
    20       30
  /   \
 40   60
Output:10 20 30 40 60

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ Number of nodes ≤ 105
1 ≤ Data of a node ≤ 105
"""

class Solution:
    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def currentLevel(self, root, level, arr):
        if root == None:
            return
        if level == 1:
            arr.append(root.data)
        if level > 1:
            self.currentLevel(root.left, level - 1, arr)
            self.currentLevel(root.right, level - 1, arr)

    def levelOrder(self, root):
        arr = []
        h = self.height(root)
        for i in range(1, h + 1, 1):
            self.currentLevel(root, i, arr)
            1
        return arr
