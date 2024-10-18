"""
Given a singly linked list.
The task is to find the length of the linked list, where length is defined as the number of nodes in the linked list.

Examples :  Input: LinkedList : 1->2->3->4->5
            Output: 5
            Explanation: Count of nodes in the linked list is 5, which is its length.

Expected Time Complexity: O(n)
Expected Auxilliary Space: O(1)

"""
class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        count = 0
        while head is not None:
            count += 1
            head = head.next
        return count

# ------- Driver code of geekforgeeks -----------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    t = int(data[0])
    for i in range(1, t + 1):
        arr = list(map(int, data[i].split()))
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        ob = Solution()
        print(ob.getCount(head))
