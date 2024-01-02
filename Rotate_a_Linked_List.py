"""
Given a singly linked list of size N.
The task is to left-shift the linked list by k nodes,
where k is a given positive integer smaller than or equal to length of the linked list.

Example 1: Input: N = 5
           value[] = {2, 4, 7, 8, 9}
           k = 3
Output: 8 9 2 4 7
Explanation: Rotate 1: 4 -> 7 -> 8 -> 9 -> 2
             Rotate 2: 7 -> 8 -> 9 -> 2 -> 4
             Rotate 3: 8 -> 9 -> 2 -> 4 -> 7

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 103
1 <= k <= N
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def rotate(self, head, k):
        current = head
        for i in range(1,k,1):
            current = current.next
            if current.next == None:
                return head
        new_head = current.next
        current.next = None
        current = new_head
        while current.next:
            current = current.next
        current.next = head
        return new_head