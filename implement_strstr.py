"""
Your task is to implement the function strstr. The function takes two strings as arguments (s,x)
and  locates the occurrence of the string x in the string s.
he function returns -1 if no match if found
else it returns an integer denoting the first occurrence of the x in the string s.

Example:
    s = GeeksForGeeks, x = For (or x=Fr return -1)
    Output: 5
"""

# first way
def strstr(s,x):
    for i in range(0,len(s),1):
        if s[i:i+len(x)]==x:
            return i
    return -1

# second way
def strstr(s,x):
    return s.find(x)