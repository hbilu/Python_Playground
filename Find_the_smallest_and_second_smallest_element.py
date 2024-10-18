"""
Given an array, arr of integers, your task is to return the smallest and second smallest element in the array.
If the smallest and second smallest do not exist, return -1.

Examples:   Input: arr[] = [2, 4, 3, 5, 6]
            Output: 2 3
            Explanation: 2 and 3 are respectively the smallest and second smallest elements in the array.

            Input: arr[] = [1, 1, 1]
            Output: -1
            Explanation: Only element is 1 which is smallest, so there is no second smallest element.

Expected Time Complexity: O(n)
Expected Auxillary Space: O(1)

Constraints:
1 <= arr.size <= 105
1 <= arr[i] <= 105
"""

class Solution:
    def minAnd2ndMin(self, arr):
        if len(arr)<2
            return [-1,-1] # Return a list so the driver code can access product[0]
        map = {}
        for i in range(len(arr)):
            if arr[i] not in map:
                map[arr[i]] = 1
            else:
                map[arr[i]] += 1
        if len(map.keys()) == 1:
            return [-1, -1] # Return a list so the driver code can access product[0]
        else:
            sorted_arr = sorted(map.keys())
        return sorted_arr[0:2]

# ------- Driver code of geekforgeeks -----------
def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        product = obj.minAnd2ndMin(arr)
        if product[0] == -1:
            print(product[0])
        else:
            print(product[0], end=" ")
            print(product[1])
        T -= 1

if __name__ == "__main__":
    main()