"""
Complete the function findOnce() which takes sorted array and its size as its input parameter
and returns the element that appears only once.
Example:
    Input: N = 11 arr[] = {1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65}
    Output: 4
"""

def findOnce(self, arr: list, n: int):
    hmap = {}
    for i in arr:
        if i not in hmap:
            hmap[i] = 1
        else:
            hmap[i] += 1
    for key, value in hmap.items():
        if value == 1:
            return key
    return -1