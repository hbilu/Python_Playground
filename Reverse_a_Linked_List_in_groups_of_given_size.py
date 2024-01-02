"""
Given a linked list of size N. The task is to reverse every k nodes in the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end,
should be considered as a group and must be reversed (See Example 2 for clarification).

Example:

Input:  LinkedList: 1->2->2->4->5->6->7->8   K = 3
Output: 2 2 1 6 5 4 8 7

Expected Time Complexity : O(N)
Expected Auxilliary Space : O(1)

Constraints:
1 <= N <= 105
1 <= k <= N
"""

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

class Solution:
    def reverse(self,head, k):
        current = head
        previous = None
        count = 0
        while current and count<k:
            following = current.next
            current.next = previous
            previous = current
            current = following
            count+=1
        if current!=None:
            head.next=self.reverse(current, k)
        return previous