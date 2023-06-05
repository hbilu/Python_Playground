"""
Implement a Queue using Linked List.
A Query Q is of 2 Types
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop an element from the queue and print the poped element)

Your Task:
Complete the function push() which takes an integer as input parameter and
pop() which will remove and return an element(-1 if queue is empty).

Expected Time Complexity: O(1).
Expected Auxiliary Space: O(1).

"""

# A linked list (LL) node
# to store a queue entry
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyQueue:
    def __init__(self):
        self.front = self.tail = None
    # Function to push an element into the queue.
    def push(self, item):
        # create Node object with item
        temp = Node(item)
        if (self.front == None and self.tail == None):
            self.front = self.tail = temp
        self.tail.next = temp
        self.tail = temp
    # Function to pop front element from the queue.
    def pop(self):
        # if self is empty
        if self.front == None:
            return -1
        if self.front == self.tail:
            elm = self.front.data
            self.front = self.tail = None
        else:
            temp = self.front
            self.front = temp.next
            elm = temp.data
        return elm