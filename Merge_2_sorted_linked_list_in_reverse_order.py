"""
Given two linked lists, which are sorted in non-decreasing order.
The task is to merge them in such a way that the resulting list is in non-increasing order.

Examples:   Input: LinkedList1 = 1->3, LinkedList2 = 2->4
            Output: 4->3->2->1

            Input: LinkedList1 = 5->10->15->40, LinkedList2 = 2->3->20
            Output: 40->20->15->10->5->3->2

Expected Time Complexity: O(n+m)
Expected Space Complexity: O(1)

Constraints:
1 <= size of the LinkedLists <= 105
0 <= node->data <= 106
"""

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''

class Solution:
    def reverseList(self, head):
        previous = None
        current = head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
    def mergeResult(self, node1, node2):
        dummy = Node(None)
        current = dummy
        while node1 and node2:
            if node1.data < node2.data:
                current.next = node1
                node1 = node1.next
            else:
                current.next = node2
                node2 = node2.next
            current = current.next
        if node1:
            current.next = node1
        elif node2:
            current.next = node2
        return self.reverseList(dummy.next)

# ------- Driver code of geekforgeeks -----------
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
    print()

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        input1 = input().split()
        input2 = input().split()
        head1, tail1 = None, None
        for item in input1:
            new_node = Node(int(item))
            if not head1:
                head1 = new_node
                tail1 = new_node
            else:
                tail1.next = new_node
                tail1 = new_node
        head2, tail2 = None, None
        for item in input2:
            new_node = Node(int(item))
            if not head2:
                head2 = new_node
                tail2 = new_node
            else:
                tail2.next = new_node
                tail2 = new_node
        ob = Solution()
        result = ob.mergeResult(head1, head2)
        print_list(result)