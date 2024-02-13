"""
Given a binary tree of size N, find its reverse level order traversal.
ie- the traversal must begin from the last level.

Example:
Input :             Output: 40 60 20 30 10              Explanation:
       10                                               Traversing level 2 : 40 60
      /  \                                              Traversing level 1 : 20 30
     20   30                                            Traversing level 0 : 10
    / \
   40  60

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 10^4

"""

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def reverseLevelOrder(root):
    if root is None:
        return
    q = []
    arr = []
    q.append(root)
    while q:
        arr.append(q[0].data)
        temp = q.pop(0)
        if temp.right:
            q.append(temp.right)
        if temp.left:
            q.append(temp.left)
    return arr[::-1] #reverse the list