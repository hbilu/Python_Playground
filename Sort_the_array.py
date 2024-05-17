'''
Given a random set of numbers, Print them in ascending sorted order.

Example: Input: n = 4, arr[] = {1, 5, 3, 2}
         Output: {1, 2, 3, 5}
         Explanation: After sorting array will be like {1, 2, 3, 5}.

Expected Time Complexity: O(n * log n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n, arr[i] ≤ 105

'''
# sorted() has O(n * log n) time complexity.
def sortArr(self, arr, n):
    return sorted(arr)

# using Merge Sort - O(n * log n)