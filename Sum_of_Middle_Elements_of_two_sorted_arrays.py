"""
Given 2 sorted arrays Ar1 and Ar2 of size N each.
Merge the given arrays and find the sum of the two middle elements of the merged array.

Example:    Input:  N = 5, Ar1[] = {1, 2, 4, 6, 10}, Ar2[] = {4, 5, 6, 9, 12}
            Output: 11
            Explanation: The merged array looks like {1,2,4,4,5,6,6,9,10,12}. Sum of middle elements is 11 (5 + 6).

Expected Time Complexity: O(log N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 103
1 <= Ar1[i] <= 106
1 <= Ar2[i] <= 106
"""

# O(log N)
class Solution:
	def findMidSum(self, ar1, ar2, n):
	    answer = []
		i=0
		j=0
		while i<n and j<n:
		    if ar1[i]<ar2[j]:
		        answer.append(ar1[i])
		        i += 1
		    else:
                answer.append(ar2[j])
		        j += 1
		answer.extend(ar1[i:])
		answer.extend(ar2[j:])
		middle = len(answer)//2
		return answer[middle-1]+answer[middle]

# O(NLogN)
class Solution:
	def findMidSum(self, ar1, ar2, n):
	    ar1.extend(ar2)
	    ar1.sort()
	    middle = len(ar1)//2
	    return ar1[middle-1]+ar1[middle]