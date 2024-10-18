"""
Given a string S, check if it is palindrome or not.

Example 1:  Input: S = "abba"   Output: 1   Explanation: S is a palindrome
Example 2:  Input: S = "abc"    Output: 0   Explanation: S is not a palindrome

Your Task:
You don't need to read input or print anything.
Complete the function isPalindrome() which takes string S as parameter
and returns an integer value 1 if it is palindrome else 0.

Constraints:
1 <= Length of S<= 2*105
"""

# first way
class Solution:
	def isPalindrome(self, S):
	    if S == S[::-1]:
	        return 1
	    return 0

# second way
class Solution:
	def isPalindrome(self, S):
	    for i in range((len(S)//2)):
	        if S[i] != S[len(S)-i-1]:
	            return 0
	    return 1

# ------- Driver code of geekforgeeks -----------
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)