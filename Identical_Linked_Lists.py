"""
Given the two singly Linked Lists respectively. The task is to check whether two linked lists are identical or not.
Two Linked Lists are identical when they have the same data and with the same arrangement too.
If both Linked Lists are identical then return true otherwise return false.

Examples:

    Input: LinkedList1: 1->2->3->4->5->6, LinkedList2: 99->59->42->20
    Output: false

    Input: LinkedList1: 1->2->3->4->5, LinkedList2: 1->2->3->4->5
    Output: true

Expected Time Complexity: O(n)
Expected Auxilliary Space: O(1)

Constraints:
1 <= length of lists <= 105
1 <= elements of lists <= 105
"""

class Solution:
    #Function to check whether two linked lists are identical or not.
    def areIdentical(self, head1, head2):
        while head1 and head2:
            if head1.data!=head2.data:
                return False
            head1 = head1.next
            head2 = head2.next
        if head1 or head2:
            return False
        return True


# ------- Driver code of geekforgeeks -----------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr1 = (int(x) for x in input().split())
        num1 = LinkedList()
        for i in arr1:
            num1.insert(i)
        arr2 = (int(x) for x in input().split())
        num2 = LinkedList()
        for i in arr2:
            num2.insert(i)
        res = Solution().areIdentical(num1.head, num2.head)
        if (res):
            print('true')
        else:
            print('false')