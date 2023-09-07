"""
Implement a Stack using two queues q1 and q2.

You are required to complete the two methods
push() which takes an integer 'x' as input denoting the element to be pushed into the stack and
pop() which returns the integer poped out from the stack(-1 if the stack is empty).

Expected Time Complexity: O(1) for push() and O(N) for pop() (or vice-versa).
Expected Auxiliary Space: O(1) for both push() and pop().

"""
# User function Template for python3
'''
    :param x: value to be inserted
    :return: None

    queue_1 = [] # first queue
    queue_2 = [] # second queue
'''

# first solution
# Time Complexity: O(N) for push() and O(1) for pop()
def push(x):
    global queue_1
    global queue_2
    queue_2.append(x)
    while queue_1:
        queue_2.append(queue_1.pop(0))
    queue_1, queue_2 = queue_2, queue_1
def pop():
    global queue_1
    global queue_2
    if queue_1:
        return queue_1.pop(0)
    return -1

# second solution
# Time Complexity: O(1) for push() and O(N) for pop()
def push(x):
    global queue_1
    global queue_2
    queue_1.append(x)
def pop():
    # global declaration
    global queue_1
    global queue_2
    if not queue_1:
        return -1
    while len(queue_1) != 1:
        queue_2.append(queue_1.pop(0))
    popped = queue_1.pop(0)
    queue_1, queue_2 = queue_2, queue_1
    return popped