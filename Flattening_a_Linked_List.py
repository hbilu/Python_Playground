
'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

'''

# print list with next pointer
def flatten(root):
    new = []
    curr_n = head
    curr_b = curr_n
    while curr_n:
        while curr_b:
            new.append(curr_b.data)
            curr_b = curr_b.bottom
        curr_b = curr_n.next
        curr_n = curr_n.next
    new = sorted(new, reverse=True)
    new_head = None
    for i in new:
        temp = Node(i)
        temp.next = new_head
        new_head = temp
    return new_head

# print list with bottom pointer
def flatten(root):
    new = []
    curr_n = head
    curr_b = curr_n
    while curr_n:
        while curr_b:
            new.append(curr_b.data)
            curr_b = curr_b.bottom
        curr_b = curr_n.next
        curr_n = curr_n.next
    new = sorted(new, reverse=True)
    new_head = None
    for i in new:
        temp = Node(i)
        temp.bottom = new_head
        new_head = temp
    return new_head