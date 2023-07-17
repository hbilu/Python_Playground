"""
Your task is to complete the function longestCommonPrefix() which takes the string array arr[] and its size N as inputs
and returns the longest common prefix common in all the strings in the array.
If there's no prefix common in all the strings, return "-1".

Example:
 Input: N=4, arr[]={geeksforgeeks,geeks,geek,geezer}
 Output: gee

Expected Time Complexity: O(N*min(|arri|)).
Expected Auxiliary Space: O(min(|arri|)) for result.
"""

def longestCommonPrefix(self, arr, n):
    arr.sort()
    com_pre = ""
    min_len = min(len(arr[0]), len(arr[n - 1]))
    index = 0
    while index < min_len and arr[0][index] == arr[n - 1][index]:
        index += 1
    com_pre = arr[0][:index]
    if com_pre == "":
        return -1
    else:
        return com_pre