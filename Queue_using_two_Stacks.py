"""
Implement a Queue using 2 stacks s1 and s2 .

You are required to complete the two methods push which take one argument an integer 'x' to be pushed into the queue
and pop which returns a integer poped out from other queue(-1 if the queue is empty).

Expected Time Complexity : O(1) for push() and O(N) for pop() or O(N) for push() and O(1) for pop()
Expected Auxilliary Space : O(1).

"""

# first solution: Time Complexity : O(1) for push() and O(N) for pop()

def Push(x, stack1, stack2):
    '''
    x: value to push, stack1: list, stack2: list
    '''
    stack1.append(x)

def Pop(stack1, stack2):
    '''
    stack1: list, stack2: list
    '''
    if not stack1:
        return -1
    while stack1:
        stack2.append(stack1.pop(-1))
    popped = stack2.pop(-1)
    while stack2:
        stack1.append(stack2.pop(-1))
    return popped

# second solution: Time Complexity : O(N) for push() and O(1) for pop()

def Push(x, stack1, stack2):
    while stack1:
        stack2.append(stack1.pop(-1))
    stack1.append(x)
    while stack2:
        stack1.append(stack2.pop(-1))

def Pop(stack1, stack2):
    if not stack1:
        return -1
    return stack1.pop(-1)