"""
Given a Binary Search Tree.
Your task is to complete the function which will return the Kth largest element
without doing any modification in Binary Search Tree.

Example:
Input: K = 1        Output: 10
       9
        \
          10

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(H) where H is max recursion stack of height H at a given time.

Constraints:
1 <= N <= 105
1 <= K <= N
"""


# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:

    def InOrder(self, root, A):
        if not root:
            return
        self.InOrder(root.left, A)
        A.append(root.data)
        self.InOrder(root.right, A)

    def kthLargest(self, root, k):
        Arr = []
        self.InOrder(root, Arr)
        return Arr[len(Arr) - k]