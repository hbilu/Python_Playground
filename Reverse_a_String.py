'''
You are given a string s. You need to reverse the string.

Example:    Input: s = Geeks    Output: skeeG

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).

Constraints:
1 <= |s| <= 10000
'''

# first way
def reverseWord(s):
    return s[::-1]

# second way
def reverseWord(s):
    s = "".join(reversed(s))
    return s