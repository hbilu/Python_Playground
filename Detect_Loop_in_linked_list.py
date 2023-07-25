"""
Given a linked list of N nodes. The task is to check if the linked list has a loop.
Linked list can contain self loop.

The task:
The task is to complete the function detectloop() which contains reference to the head as only argument.
This function should return true if linked list contains loop, else return false.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""

# Node Class (which is given with the task)
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None

# first soluiton
class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):
        front = head
        tail = head
        while (front and tail and tail.next):
            front = front.next
            tail = tail.next.next
            if front == tail:
                return True
        return False

# second solution: using hashing
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        hashset = set()
        temp = head
        while (temp != None):
            if temp in hashset:
                return True
            else:
                hashset.add(temp)
                temp = temp.next
        return False

