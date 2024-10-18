"""
Given a singly linked list. The task is to remove duplicates (nodes with duplicate values)
from the given list (if it exists).
Note: Try not to use extra space. The nodes are arranged in a sorted way.

Examples:   Input: LinkedList: 2->2->4->5
            Output: 2 -> 4 -> 5
            Explanation: In the given linked list 2 -> 2 -> 4 -> 5, only 2 occurs more than 1 time.
                         So we need to remove it once.

Expected Time Complexity : O(n)
Expected Space Complexity: O(1)

Constraints:
1 <= Number of nodes, data of nodes <= 105
"""

def removeDuplicates(head):
    current = head
    while current.next:
        if current.data == current.next.data:
            # Correctly link to the node after the duplicate
            current.next = current.next.next
        else:
            # Move to the next node only if no duplicate is found
            current = current.next
    return head

# ------- Driver code of geekforgeeks -----------
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # creates a new node with given value and appends it at the end of the
    #linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print('')

if __name__ == '__main__':
    t = int(input())
    for cases in range(t):

        a = LinkedList()  # create a new linked list 'a'.
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        removeDuplicates(a.head)
        a.printList()