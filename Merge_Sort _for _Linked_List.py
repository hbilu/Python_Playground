"""
Given Pointer/Reference to the head of the linked list, the task is to Sort the given linked list using Merge Sort.
Note: If the length of linked list is odd, then the extra node should go in the first list while splitting.

Example :
    Input:  N = 5  value[]  = {3,5,2,4,1}
    Output: 1 2 3 4 5
    Explanation: After sorting the given linked list, the resultant matrix will be 1->2->3->4->5.

Expected Time Complexity: O(N*Log(N))
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 105
"""

'''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list

    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''

class Solution:
    def getMid(self, head):
        slow = head
        fast = head
        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortedMerge(self, a, b):
        result = Node(0)
        temp = result
        if a == None:
            return b
        if b == None:
            return a
        while (a != None and b != None):
            if a.data <= b.data:
                temp.next = a
                a = a.next
            else:
                temp.next = b
                b = b.next
            temp = temp.next
        if a != None:
            temp.next = a
        else:
            temp.next = b
        return result.next

    def mergeSort(self, head):
        if head == None or head.next == None:
            return head
        middle = self.getMid(head)
        next_to_middle = middle.next
        middle.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(next_to_middle)
        sortedlist = self.sortedMerge(left, right)
        return sortedlist