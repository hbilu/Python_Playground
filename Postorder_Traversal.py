"""
Given a binary tree, find the Postorder Traversal of it.

Example:
    Input:              Output: 11 13 10 8 19
            19
         /     \
        10      8
      /    \
     11    13

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= Number of nodes <= 105
0 <= Data of a node <= 106
"""
def postOrder(root):
    arr = []
    if root:
        arr += postOrder(root.left)
        arr += postOrder(root.right)
        arr.append(root.data)
    return arr