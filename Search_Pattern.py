"""
Given two strings, one is a text string txt and the other is a pattern string pat.
The task is to print the indexes of all the occurrences of the pattern string in the text string.
Use 0-based indexing while returning the indices.
Note: Return an empty list in case of no occurrences of pattern.

Examples :

    Input: txt = "abcab", pat = "ab"
    Output: [0, 3]
    Explanation: The string "ab" occurs twice in txt, one starts at index 0 and the other at index 3.

    Input: txt = "aabaacaadaabaaba", pat = "aaba"
    Output: [0, 9, 12]

Constraints:
1 ≤ txt.size() ≤ 106
1 ≤ pat.size() < txt.size()
Both the strings consist of lowercase English alphabets.

"""

class Solution:
    def search(self, pat, txt):
        Ltext = len(txt)
        Lpat = len(pat)
        result = []
        for i in range(Ltext-Lpat+1):
            if txt[i:i+Lpat] == pat:
                result.append(i)
        return result

# ------- Driver code of geekforgeeks -----------
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()