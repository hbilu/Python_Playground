"""
Your Task:
 are required to complete two methods push() and pop(). T
 he push() method takes one argument, an integer 'x' to be pushed into the stack and
 pop() which returns an integer present at the top and popped out from the stack.
 If the stack is empty then return -1 from the pop() method.

Expected Time Complexity: O(1) for both push() and pop().
Expected Auxiliary Space: O(1) for both push() and pop()

"""

class StackNode:
    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:

    def __init__(self):
        self.head = None

    # Function to push an integer into the stack.
    def push(self, data):
        newnode = StackNode(data)
        newnode.next = self.head
        self.head = newnode

    # Function to remove an item from top of the stack.
    def pop(self):
        if self.head == None:
            return -1
        poppednode = self.head
        self.head = self.head.next
        poppednode.next = None
        return poppednode.data