"""
Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only.
The task is to segregate 0s, 1s, and 2s linked list such that all zeros segregate to head side,
2s at the end of the linked list, and 1s in the mid of 0s and 2s.

Example:
   Input: N = 8
   value[] = {1,2,2,1,2,0,2,2}
   Output: 0 1 1 2 2 2 2 2

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints: 1 <= N <= 106
"""

class Node:
	def __init__(self, data):   # data -> value stored in node
		self.data = data
		self.next = None
class Solution:
    def segregate(self, head):
        if head==None or head.next==None:
            return head
        current = head
        end = head
        previous = None
        index = 0
        length = 0
        while end.next!=None:
            length += 1
            end = end.next
        while index <= length:
            if current.data==0 and previous!=None:
                    following = current.next
                    previous.next = following
                    current.next = head
                    head = current
                    current = following
            elif current.data==2:
                if previous==None:
                    following = current.next
                    head = following
                    current.next = None
                    end.next = current
                    current = following
                    end = end.next
                elif current.next!=None:
                    following = current.next
                    previous.next = following
                    current.next = None
                    end.next = current
                    current = following
                    end = end.next
            else:
                previous = current
                current = current.next
            index += 1
        return head