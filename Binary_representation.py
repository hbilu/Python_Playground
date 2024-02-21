"""
Write a program to print Binary representation of a given number N.

Example 1:  Input:  N = 2
            Output: 000000000000000000000000000010
            Explanation: The binary representation of 2 is '10' but we need to print in 30 bits so append
                         remaining 0's in the left.

Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 10^9
"""

class Solution:
	def getBinaryRep(self, n):
		return bin(n).replace("0b","0"*(32-len(bin(n))))