"""
Your task is to implement  2 stacks in one array efficiently. You need to implement 4 methods.

twoStacks : Initialize the data structures and variables to be used to implement  2 stacks in one array.
push1 : pushes element into first stack.
push2 : pushes element into second stack.
pop1 : pops element from first stack and returns the popped element. If first stack is empty, it should return -1.
pop2 : pops element from second stack and returns the popped element. If second stack is empty, it should return -1.

Example 1:
    Input: push1(2) push1(3) push2(4) pop1() pop2() pop2()
    Output: 3 4 -1
Explanation:    push1(2) the stack1 will be {2}
                push1(3) the stack1 will be {2,3}
                push2(4) the stack2 will be {4}
                pop1()   the poped element will be 3 from stack1 and stack1 will be {2}
                pop2()   the poped element will be 4 from stack2 and now stack2 is empty
                pop2()   the stack2 is now empty hence returned -1.

Expected Time Complexity: O(1) for all the four methods.
Expected Auxiliary Space: O(1) for all the four methods.

Constraints:
1 <= Number of queries <= 104
1 <= Number of elements in the stack <= 100
The sum of count of elements in both the stacks < size of the given array
"""

class TwoStacks:
    def __init__(self, n=100):
        self.n = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = n

    def push1(self, x):
        self.top1+=1
        self.arr[self.top1] = x

    def push2(self, x):
        self.top2-=1
        self.arr[self.top2] = x

    def pop1(self):
        if self.top1 == -1:
            return -1
        temp = self.arr[self.top1]
        self.arr[self.top1] = None
        self.top1 -= 1
        return temp

    def pop2(self):
        if self.top2 == self.n:
            return -1
        temp = self.arr[self.top2]
        self.arr[self.top2] = None
        self.top2 += 1
        return temp