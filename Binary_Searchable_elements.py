"""
Binary search is a search algorithm usually used on a sorted sequence to quickly find an element with a given value.
In this problem we will evaluate how binary search performs on data that isn't necessarily sorted.
An element is said to be binary searchable if, regardless of how the pivot is chosen the algorithm returns true.

Example:    Input: N = 6, arr[] = {2, 1, 3, 5, 4, 6}
            Output: 2
            Explanation: 3 and 6 are the numbers guaranteed to be found in the same way.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ N ≤ 105
1 ≤ arr[i] ≤ 105
"""

# first way - O(N*log(N))
class Solution:
    def binarySearchable(self, Arr, n):
        count = 0
        for i in range(n):
            start = 0
            end = n-1
            while (start<=end):
                middle = int((start+end)/2)
                if Arr[middle] == Arr[i]:
                    count += 1
                elif Arr[middle] < Arr[i]:
                    end = middle+1
                elif Arr[middle] > Arr[i]:
                    start = middle-1
        return count

# second way - O(N)
    class Solution:
        def binarySearchable(self, Arr, n):
            maxLeft = [0] * n
            minRight = [0] * n
            maxLeftVal = -1e5
            minRightVal = 1e5
            count = 0
            for i in range(0, n, 1):
                maxLeft[i] = maxLeftVal
                maxLeftVal = max(maxLeftVal, Arr[i])
            for i in range(n - 1, -1, -1):
                minRight[i] = minRightVal
                minRightVal = min(minRightVal, Arr[i])
            for i in range(n):
                if Arr[i] > maxLeft[i] and Arr[i] < minRight[i]:
                    count += 1
            return count