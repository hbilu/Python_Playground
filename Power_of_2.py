"""
Given a non-negative integer N.
The task is to check if N is a power of 2.
More formally, check if N can be expressed as 2x for some integer x.

Example:
    Input: N = 8
    Output: YES
    Explanation: 8 is equal to 2 raised to 3 (23 = 8).

Expected Time Complexity:O(log N).
Expected Auxiliary Space:O(1).
"""

# first way: using bitwise & operator

def isPowerofTwo(self, n):
    if n == 0:
        return False
    elif (n & (n - 1)) == 0:
        return True
    elif (n & (n - 1)) != 0:
        return False

# second way: using % and // arithmetic operators

def isPowerofTwo(self,n):
    while (n!=1):
        if (n%2!=0):
            return False
        n//=2
    return True
