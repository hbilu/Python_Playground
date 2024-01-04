"""
Given a binary tree. Find the inorder traversal (Left->Root->Right) of the tree without using recursion.

Example:
    Input:              Output: 4 2 5 1 3
               1
             /    \
           2       3
          /   \
        4     5

Expected time complexity: O(N)
Expected auxiliary space: O(N)

Constraints:
1 <= Number of nodes <= 105
1 <= Data of a node <= 105
"""
class Solution:
    def inOrder(self, root):
        current = root
        arr = []
        stack = []
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                arr.append(current.data)
                current = current.right
            else:
                break
        return arr