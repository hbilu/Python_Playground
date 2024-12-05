"""
Given an array arr consisting of positive integer numbers, remove all duplicate numbers.

Example:
    Input: arr[] = [2, 2, 3, 3, 7, 5]
    Output: [2, 3, 7, 5]

    Explanation: After removing the duplicates 2 and 3 we get 2 3 7 5.
    Input: arr[] = [2, 2, 5, 5, 7, 7]
    Output: [2, 5, 7]
Constraints:
1<= arr.size() <=106
2<= arr[i] <=100
"""

# first way: preserving the original sequence of numbers (which is required to pass this problem on geekforgeeks)
class Solution:
    def removeDuplicates(self, arr):
        seen = set()
        result = []
        for num in arr:
            if num not in seen:
                seen.add(num)
                result.append(num)
        return result

# second way: if preserving the original sequence is not required
class Solution:
    def removeDuplicates(self, arr):
        return list(set(arr))

# ------- Driver code of geekforgeeks -----------
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.removeDuplicates(arr)
        print(*ans)
        print("~")
        t -= 1