"""
Given a linked list of N nodes. The task is to reverse this list and return new head after reversing the list.

Example:
    Input: LinkedList: 2->7->8->9->10
    Output: 10 9 8 7 2
    Explanation: After reversing the list, elements are 10->9->8->7->2.

"""
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        current = head
        previous = None
        while current != None:
            following = current.next
            current.next = previous
            previous = current
            current = following
        return previous