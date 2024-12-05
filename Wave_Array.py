"""
Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array(In Place).
In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....
If there are multiple solutions, find the lexicographically smallest one.

Note: The given array is sorted in ascending order, and you don't need to return anything to change the original array.

Examples:   Input: arr[] = [1, 2, 3, 4, 5]
            Output: [2, 1, 4, 3, 5]
            Explanation: Array elements after sorting it in the waveform are 2, 1, 4, 3, 5.

            Input: arr[] = [2, 4, 7, 8, 9, 10]
            Output: [4, 2, 8, 7, 10, 9]
            Explanation: Array elements after sorting it in the waveform are 4, 2, 8, 7, 10, 9.

Constraints:
1 ≤ arr.size ≤ 106
0 ≤ arr[i] ≤107
"""

class Solution:
    def convertToWave(self, arr: List[int]) -> None:
        for i in range(0, len(arr) - 1, 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

# ------- Driver code of geekforgeeks -----------
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        obj.convertToWave(arr)
        IntArray().Print(arr)
        print("~")