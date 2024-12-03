"""
Given a string s consisting of lowercase Latin Letters. Return the first non-repeating character in s.
If there is no non-repeating character, return '$'.
Note: When you return '$' driver code will output -1.

Examples:

    Input: s = "geeksforgeeks"
    Output: 'f'
    Explanation: In the given string, 'f' is the first character in the string which does not repeat.

    Input: s = "racecar"
    Output: 'e'
    Explanation: In the given string, 'e' is the only character in the string which does not repeat.

Constraints:
1 <= s.size() <= 105
"""

class Solution:
    def nonRepeatingChar(self, s):
        hashmap = {}
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        for char in s:
            if hashmap[char] == 1:
                return char
        return -1


# ------- Driver code of geekforgeeks -----------

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        ans = obj.nonRepeatingChar(s)
        if (ans != '$'):
            print(ans)
        else:
            print(-1)
        print("~")
