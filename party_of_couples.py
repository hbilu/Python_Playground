"""
Your task is to complete the function findSingle() which takes the size of the array N
and the array arr[] as input parameters and returns the only single person.

Example:
    Input: N = 11
    arr = {1, 2, 3, 5, 3, 2, 1, 4, 5, 6, 6}
    Output: 4
    Explaination: 4 is the only single.
"""

def findSingle(self, N, arr):
    hmap = {}
    for i in arr:
        if i not in hmap:
            hmap[i] = 1
        else:
            hmap[i] += 1
    for key, value in hmap.items():
        if value == 1:
            return key