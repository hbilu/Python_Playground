"""
Given two strings A and B consisting of lowercase english characters.
Find the characters that are not common in the two strings.

Example:
    Input: A = characters B = alphabets
    Output: bclpr
"""

def UncommonChars(self, A, B):
    set_A = set(A)
    set_B = set(B)
    diff_U = set_A.difference(set_B).union(set_B.difference(set_A))
    str_U = ''.join(sorted(diff_U))
    if str_U:
        return str_U
    return -1