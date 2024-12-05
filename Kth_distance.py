"""
Given an unsorted array arr and a number k which is smaller than the size of the array.
Return true if the array contains any duplicate within k distance throughout the array else false.

Examples:   Input: arr[] = [1, 2, 3, 4, 1, 2, 3, 4], k = 3
            Output: false
            Explanation: All duplicates are more than k distance away.

            Input: arr[] = [1, 2, 3, 1, 4, 5], k = 3
            Output: true
            Explanation: 1 is repeated at distance 3.

            Input: arr[] = [6, 8, 4, 1, 8, 5, 7], k = 3
            Output: true
            Explanation: 8 is repeated at distance 3.
Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ k < arr.size()
1 ≤ arr[i] ≤ 105
"""

# first
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        for i in range(len(arr)):
            subset = arr[i + 1:i + k + 1]
            if arr[i] in subset:
                return True
        return False

# second
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        seen = set()
        for i in range(len(arr)):
            if arr[i] in seen:
                return True
            seen.add(arr[i])
            if len(seen) > k:
                seen.remove(arr[i - k])
        return False

# ------- Driver code of geekforgeeks -----------
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.checkDuplicatesWithinK(arr, k)
        if res:
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1