"""
Your Task:
You are required to complete two methods push() and pop().
The push() method takes one argument, an integer 'x' to be pushed into the stack
and pop() which returns an integer present at the top and popped out from the stack.
If the stack is empty then return -1 from the pop() method.

Expected Time Complexity : O(1) for both push() and pop().
Expected Auixilliary Space : O(1) for both push() and pop().

Constraints:
1 <= Q <= 100
1 <= x <= 100
"""

# without considering the constraint for array size
class MyStack:
    def __init__(self):
        self.arr = []
    def push(self, data):
        self.arr.append(data)
    def pop(self):
        if self.arr == None:
            return -1
        data = self.arr[-1]
        return data

# with regard of constraint of array size <- accepted by Geek for Geeks
class MyStack:
    def __init__(self):
        self.array_size = 100
        self.arr = [0] * self.array_size
        self.top = -1
    def push(self, data):
        if self.top == self.array_size - 1:
            self.arr += [0] * self.array_size
        self.top += 1
        self.arr[self.top] = data
    def pop(self):
        data = -1
        if self.top > -1:
            data = self.arr[self.top]
            self.top -= 1
        return data
