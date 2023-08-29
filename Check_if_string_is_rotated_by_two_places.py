"""
Given two strings a and b. The task is to find if the string 'b' can be obtained by rotating another string 'a'
by exactly 2 places.

Example:
    Input: a = amazon b = azonam
    Output: 1
    Explanation: amazon can be rotated anticlockwise by two places, which will make it as azonam.

Expected Time Complexity: O(N).
Expected Auxilary Complexity: O(N).
Challenge: Try doing it in O(1) space complexity.
"""


def isRotated(self, str1, str2):
    if len(str1) != len(str2):
        return False
    if len(str1) < 2:
        return str1 == str2
    c_rot = ""
    ac_rot = ""
    # clockwise rotation 2 times
    c_rot = c_rot + str2[2:] + str2[:2]
    # anticlockwise rotation 2 times
    ac_rot = ac_rot + str2[len(str2) - 2:] + str2[:len(str2) - 2]
    return (c_rot == str1 or ac_rot == str1)