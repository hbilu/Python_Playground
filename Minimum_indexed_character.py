"""
Your Task:
You only need to complete the function minIndexChar() that returns the index of answer in str or
returns -1 in case no character of pat is present in str.

Example:
    Input: str = geeksforgeeks
    pat = set
Output: 1
Explanation: e is the character which is present in given str "geeksforgeeks" and is also presen in pat "set". Minimum
index of e is 1.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Number of distinct characters).
"""

def minIndexChar(self, Str, pat):
    lStr = list(Str)
    for i in range(0, len(lStr), 1):
        index = pat.find(lStr[i])
        if index >= 0:
            return i
    return -1