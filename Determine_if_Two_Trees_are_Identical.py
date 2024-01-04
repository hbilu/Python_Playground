"""
Given two binary trees, the task is to find if both of them are identical or not.

Example:
    Input:                  Output: Yes
         1          1
       /   \      /   \
      2     3    2     3
    Input:                  Output: No
        1       1
      /  \     /  \
     2    3   3    2

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 <= Number of nodes <= 105
1 <=Data of a node <= 109
"""
class Solution:
    def isIdentical(self,root1, root2):
        if root1 == None and root2 == None: #to compare NULL leaves
            return True
        if root1 and root2:
            return (root1.data == root2.data) and self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)
        return False