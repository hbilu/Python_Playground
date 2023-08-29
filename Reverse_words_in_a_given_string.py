"""
Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

Example:
    Input: S = i.like.this.program.very.much
    Output: much.very.program.this.like.i
    Explanation: After reversing the whole string(not individual words), the input string becomes
                much.very.program.this.like.i

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)

"""

def reverseWords(self, S):
    S_reversed = []
    S_words = S.split('.')
    while S_words:
        S_reversed.append(S_words.pop())
    SR = '.'.join(S_reversed)
    return SR