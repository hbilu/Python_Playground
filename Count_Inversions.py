"""
Given an array of integers. Find the Inversion Count in the array.

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted.
If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum.
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Example:    Input: N = 5, arr[] = {2, 4, 1, 3, 5}
            Output: 3
            Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (4, 1), (2, 1), (4, 3).

Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 5*105
1 ≤ arr[i] ≤ 1018
"""

# by using merge sort

class Solution:

    def merge(self, left, right):
        i = j = count = 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                # counting inversions: min value right will swap len(left)-i times because len(left) is sorted
                count += len(left) - i
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, count

    def mergeSortAndCount(self, A):
        if len(A) <= 1:
            return A, 0
        middle = len(A) // 2
        left, left_count = self.mergeSortAndCount(A[:middle])
        right, right_count = self.mergeSortAndCount(A[middle:])
        merged, merge_count = self.merge(left, right)
        return merged, left_count + right_count + merge_count

    def inversionCount(self, arr, n):
        _, count = self.mergeSortAndCount(arr)
        return count

