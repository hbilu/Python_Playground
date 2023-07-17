"""
Your task is to complete the function isAnagram() which takes the string a and string b as input parameter
and check if the two strings are an anagram of each other.
The function returns true if the strings are anagram else it returns false.

An anagram of a string is another string that contains the same characters,
only the order of characters can be different.

Example:
 Input:a = geeksforgeeks, b = forgeeksgeeks
 Output: YES
 Input:a = allergy, b = allergic
 Output: NO

Expected Time Complexity:O(|a|+|b|).
Expected Auxiliary Space: O(Number of distinct characters).
"""
def isAnagram(self, a, b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False