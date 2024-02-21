"""
Given coordinates of 2 points on a cartesian plane, find the distance between them rounded up to nearest integer.

Example 1:  Input: 0 0 2 -2
            Output: 3
            Explanation: Distance between (0, 0) and (2, -2) is 3.

Expected Time Complexity: O(1)
Expected Space Complexity: O(1)

Constraints:
-1000 <= x1, y1, x2, y2 <= 1000
"""

# first way:
class Solution:
	def distance(self, x1, y1, x2, y2):
		return round(((x1-x2)**2 + (y1-y2)**2)**0.5)