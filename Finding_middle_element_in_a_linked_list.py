"""
Given a singly linked list of N nodes.
The task is to find the middle of the linked list. For example, if the linked list is
1-> 2->3->4->5, then the middle node of the list is 3.
If there are two middle nodes(in case, when N is even), print the second middle element.
For example, if the linked list given is 1->2->3->4->5->6, then the middle node of the list is 4.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

"""

class node:
    def __init__(data):
        self.data = data
        self.next = None

class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    # first solution
    def findMid(self, head):
        D = []
        temp = head
        while temp != None:
            D.append(temp.data)
            temp=temp.next
        return D[int(len(D)/2)]

    # second solution
    def findMid(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    # third solution
    def findMid(self, head):
        count = 0
        middle = head
        while head:
            # if count is an odd number:
            # 'count&1' evaluates to true if the last bit in the binary form of 'count' is equal to 1
            if count & 1:
                middle = middle.next
            count += 1
            head = head.next
        return middle.data