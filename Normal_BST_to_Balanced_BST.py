"""
Given a Binary Search Tree, modify the given BST such that it is balanced and has minimum possible height.
Return the balanced BST.

Example:

Input:
         4
        /
       3
      /
     2
    /
   1
Output:
      3            3           2
    /  \         /  \        /  \
   1    4   OR  2    4  OR  1    3
    \          /                  \
     2        1                    4

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Here N denotes total number of nodes in given BST.

Constraints:
1 <= N <= 105
1 <= Node data <= 109
"""


class Solution:

    def inorder(self, root, ans):
        if root == None:
            return
        self.inorder(root.left, ans)
        ans.append(root.data)
        self.inorder(root.right, ans)

    def arrayBST(self, ans, start, end):
        if (start > end):
            return None
        mid = (start + end) // 2
        temp = Node(int(ans[mid]))
        temp.left = self.arrayBST(ans, start, mid - 1)
        temp.right = self.arrayBST(ans, mid + 1, end)
        return temp

    def buildBalancedTree(self, root):
        # code here
        ans = []
        self.inorder(root, ans)
        return self.arrayBST(ans, 0, len(ans) - 1)