"""
Given a singly linked list's head. Your task is to complete the function alternatingSplitList()
that splits the given linked list into two smaller lists.
The sublists should be made from alternating elements from the original list.

Examples:   Input: LinkedList = 0->1->0->1->0->1
            Output: 0->0->0 , 1->1->1

            Input: LinkedList = 2->5->8->9->6
            Output: 2->8->6 , 5->9

Constraints:
1 <= number of nodes <= 100
1 <= node -> data <= 104
"""

class Solution:
    def alternatingSplitList(self, head):
        if not head:
            return None
        temp = head
        list1 = None
        list2 = None
        current1 = None
        current2 = None
        while temp and temp.next:
            if list1 is None:
                list1 = Node(temp.data)
                current1 = list1
            else:
                current1.next = Node(temp.data)
                current1 = current1.next
            if list2 is None:
                list2 = Node(temp.next.data)
                current2 = list2
            else:
                current2.next = Node(temp.next.data)
                current2 = current2.next
            temp = temp.next.next
        if temp:
            current1.next = Node(temp.data)
            current1 = current1.next
        return list1, list2

# ------- Driver code of geekforgeeks -----------
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = Node(arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next
        ob = Solution()
        result = ob.alternatingSplitList(head)
        printList(result[0])
        printList(result[1])