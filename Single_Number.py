"""
Given an array arr[] of positive integers where every element appears even times except for one.
Find that number occurring an odd number of times.

Examples:   Input: arr[] = [1, 1, 2, 2, 2]
            Output: 2
            Explanation: In the given array all element appear two times except 2 which appears thrice.

            Input: arr[] = [8, 8, 7, 7, 6, 6, 1]
            Output: 1
            Explanation: In the given array all element appear two times except 1 which appears once.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arri ≤ 105
"""

# first way
class Solution:
    def getSingle(self,arr):
        map = {}
        for i in range(len(arr)):
            if arr[i] not in map:
                map[arr[i]] = 1
            else:
                map[arr[i]] += 1
        for key, value in map.items():
            if value % 2 != 0:
                return key

# second way - This code uses XOR to cancel out duplicates and isolate the single non-duplicate element.
class Solution:
    def getSingle(self, arr):
        ans = 0
        # XOR all elements in the array x^0=x x^x=0
        for i in arr:
            ans ^= i
        # After all XOR operations, ans will hold the single element
        return ans


# ------- Driver code of geekforgeeks -----------
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        # k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getSingle(arr)
        print(res)
        t -= 1