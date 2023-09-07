"""
The task is to swap elements in the linked list pairwise.

Example:
    Input: LinkedList: 1->3->4->7->9->10->1
    Output: 3 1 7 4 10 9 1
    Explanation: After swapping each pair considering (1,3), (4, 7), (9, 10)..
                so on as pairs, we get 3, 1, 7, 4, 10, 9, 1 as a new linked list.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
"""

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

class Solution:
    def pairWiseSwap(self, head):
        if head==None or head.next==None:
            return head
        current = head
        previous = None
        following = None
        while current!=None and current.next!=None:
            following  = current.next
            if previous == None:
                head = following
            else:
                previous.next = following
            current.next = following.next
            following.next = current
            previous = current
            current = current.next
        return head