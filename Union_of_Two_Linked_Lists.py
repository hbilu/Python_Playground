"""
Given two linked lists (L1 & L2), your task is to complete the function makeUnion(),
which returns the union list of two linked lists.
This union list should include all the distinct elements only and it should be sorted in ascending order.

Examples:   Input: L1 = 9->6->4->2->3->8, L2 = 1->2->8->6->2
            Output: 1 -> 2 -> 3 -> 4 -> 6 -> 8 -> 9

Expected Time Complexity: O((n+m)*Log(n+m))
Expected Space Complexity: O(n+m)

Constraints:
1<=size of both linked lists<=105
1<= data of nodes<=105
"""

class Solution:
    def union(self, head1,head2):
        unique_numbers = set()
        while head1:
            unique_numbers.add(head1.data)
            head1 = head1.next
        while head2:
            unique_numbers.add(head2.data)
            head2 = head2.next
        sorted_numbers = sorted(unique_numbers)
        dummy = Node(None)
        current = dummy
        for num in sorted_numbers:
            current.next = Node(num)
            current = current.next
        return dummy.next

# ------- Driver code of geekforgeeks -----------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next

if __name__ == '__main__':
    for _ in range(int(input())):
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        ob = Solution()
        printList(ob.union(ll1.head, ll2.head))
        print()
        print("~")