
"""
Your task is to return the data stored in the nth node from end of linked list.

Function Arguments: head (reference to head of the list), n (pos of node from end)
Return Type: Integer or -1 if no such node exits.

{
	# Node Class
	class Node:
		def __init__(self, data):   # data -> value stored in node
		    self.data = data
		    self.next = None
	}
"""


# Function to find the data of nth node from the end of a linked list
def getNthFromLast(head, n):
    temp = head
    L = 0
    while temp != None:
        L += 1
        temp = temp.next
    if n > L:
        return -1
    temp = head
    for index in range(1, L - n + 1):
        temp = temp.next
    return temp.data