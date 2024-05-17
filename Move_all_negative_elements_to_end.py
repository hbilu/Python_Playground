'''
Given an unsorted array arr[] of size n having both negative and positive integers.
The task is place all negative element at the end of array
without changing the order of positive element and negative element.

Example:    Input : n = 8, arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
            Output : 1  3  2  11  6  -1  -7  -5

Your Task:
Your task is to complete the function segregateElements() which takes the array arr[] and its size N as inputs
and store the answer in the array arr[] itself.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ n ≤ 106
-109 ≤ arr[i] ≤ 109
'''

class Solution:
    def segregateElements(self, arr, n):
        pos = []
        neg = []
        for i in range(n):
            if arr[i]<0:
                neg.append(arr[i])
            else:
                pos.append(arr[i])
        arr.clear()
        arr.extend(pos+neg)
        return arr