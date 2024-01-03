"""
Given a linked list of N nodes such that it may contain a loop.
A loop here means that the last node of the link list is connected to the node at position X(1-based index).
If the link list does not have any loop, X=0.
Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.

Example:

Input:  N = 4  value[] = {1,2,3,4}  X = 1
Output: 1
Explanation: The link list looks like
1 -> 2 -> 3 -> 4
^              |
|______________|

Expected time complexity: O(N)
Expected auxiliary space: O(1)

Constraints:
1 ≤ N ≤ 10^4

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

"""

# first solution: using hashing
class Solution:
    def removeLoop(self, head):
        hashset = set()
        temp = head
        previous = None
        while temp != None:
            if temp in hashset:
                previous.next = None
                return True
            else:
                hashset.add(temp)
                previous = temp
                temp = temp.next
        return False

# second solution with Floyd’s Cycle-Finding Algorithm

