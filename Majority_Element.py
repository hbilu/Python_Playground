"""
Given an array arr. Find the majority element in the array. If no majority exists, return -1.

A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array.

Examples:

    Input: arr[] = [3, 1, 3, 3, 2]
    Output: 3
    Explanation: Since, 3 is present more than n/2 times, so it is the majority element.

    Input: arr[] = [7]
    Output: 7
    Explanation: Since, 7 is single element and present more than n/2 times, so it is the majority element.

    Input: arr[] = [2, 13]
    Output: -1
    Explanation: Since, no element is present more than n/2 times, so there is no majority element.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i]≤ 105

"""

class Solution:
    def majorityElement(self, arr):
        limit = len(arr) // 2
        hashmap = {}  # Using a dictionary to store counts
        for num in arr:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
            if hashmap[num] > limit:  # Early exit if majority found
                return num
        return -1  # No majority element found

# ------- Driver code of geekforgeeks -----------
import math
from sys import stdin
def main():
    T = int(input())
    while (T>0):
        A = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.majorityElement(A))
        T -= 1
if __name__ == "__main__":
    main()