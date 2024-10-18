"""
You are given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
If there are no such elements return an empty array. In this case, the output will be -1.

Examples :  Input: arr1 = [1, 5, 10, 20, 40, 80] , arr2 = [6, 7, 20, 80, 100] , arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
            Output: [20, 80]
            Explanation: 20 and 80 are the only common elements in arr, brr and crr.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Here n = Total sizes of arr1, arr2, and arr3
"""

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        set_arr1 = set(arr1)
        set_arr2 = set(arr2)
        set_arr3 = set(arr3)
        common_set = set_arr1.intersection(set_arr2).intersection(set_arr3)
        list_common = sorted(common_set)
        return list_common if list_common else [-1]

# ------- Driver code of geekforgeeks -----------
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        brr = list(map(int, input().split()))
        crr = list(map(int, input().split()))
        ob = Solution()
        res = ob.commonElements(arr, brr, crr)
        if len(res) == 0:
            print(-1)
        else:
            print(" ".join(map(str, res)))