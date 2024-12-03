"""
Given a string s, the task is to find the minimum characters to be added at the front to make the string palindrome.

Note: A palindrome string is a sequence of characters that reads the same forward and backward.

Examples:
    Input: s = "abc"
    Output: 2
    Explanation: Add 'b' and 'c' at front of above string to make it palindrome : "cbabc"

Constraints:
1 <= s.size() <= 106
"""

# first way: O(n2) time complexity
class Solution:
    def isPalindrome(self, x):
        return x == x[::-1]

    def minChar(self, s):
        num = 0
        while not self.isPalindrome(s):
            s = s[-1] + s
            num += 1
        return num

# second way: O(n) time complexity with LPS: Longest Prefix Suffix
class Solution:
    def minChar(self, s: str) -> int:
        temp = s + "#" + s[::-1]
        n = len(temp)
        # Initialize the LPS array (Longest Prefix Suffix array) with zeros.
        # LPS will store the length of the longest prefix of 'temp' that matches a suffix.
        lps = [0] * n
        j = 0
        for i in range(1, n):
            # If there's a mismatch, backtrack using the LPS array to find the next best prefix to compare with.
            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]
            # If the characters match, we increment the length of the current prefix
            if temp[i] == temp[j]:
                j += 1
            lps[i] = j
        # The last value of the LPS array gives the length of the longest palindromic prefix
        longest_palindromic_prefix = lps[-1]
        return len(s) - longest_palindromic_prefix

# ------- Driver code of geekforgeeks -----------
if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")