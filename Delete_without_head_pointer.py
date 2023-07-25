"""
You are given a pointer/ reference to the node which is to be deleted from the linked list of N nodes.
The task is to delete the node if it not the tail node.

Example:
    Input: value[] = {10,20,4,30} node = 20
    Output: 10 4 30
    Explanation: After deleting 20 from the linked list, we have remaining nodes as 10, 4 and 30.
"""
class Node:
	def __init__(self, data):   # data -> value stored in node
		self.data = data
	    self.next = None

class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,curr_node):
        if curr_node.next != None:
            curr_node.data = curr_node.next.data
            curr_node.next = curr_node.next.next