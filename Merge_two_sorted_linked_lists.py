"""
Given two sorted linked lists consisting of N and M nodes respectively.
The task is to merge both of the list (in-place) and return head of the merged list.

Example:
    Input:
        N = 4, M = 3
        valueN[] = {5,10,15,40}
        valueM[] = {2,3,20}
    Output: 2 3 5 10 15 20 40
    Explanation: After merging the two linked lists, we have merged list as 2, 3, 5, 10, 15, 20, 40.

Expected Time Complexity : O(n+m)
Expected Auxilliary Space : O(1)

Constraints:
1 <= N, M <= 104
0 <= Node's data <= 105

class Node:
	def __init__(self, data):   # data -> value stored in node
		self.data = data
		self.next = None
"""
# using Brute Force Way
def sortedMerge(head1, head2):
    new = []
    while head1 != None:
        new.append(head1.data)
        head1 = head1.next
    while head2 != None:
        new.append(head2.data)
        head2 = head2.next
    new = sorted(new, reverse=True)
    new_head = None
    for i in new:
        temp = Node(i)
        temp.next = new_head
        new_head = temp
    return new_head

# using dummy node
def sortedMerge(head1, head2):
    new_head = Node(0)
    tail = new_head
    while True:
        if head1 is None:
            tail.next = head2
            break
        if head2 is None:
            tail.next = head1
            break
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    return new_head.next
