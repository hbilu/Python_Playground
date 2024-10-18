"""
Given a permutation of some of the first natural numbers in an array arr[],
determine if the array can be sorted in exactly two swaps. A swap can involve the same pair of indices twice.

Return true if it is possible to sort the array with exactly two swaps, otherwise return false.

Examples:   Input: arr = [4, 3, 2, 1]
            Output: true
            Explanation:    First, swap arr[0] and arr[3]. The array becomes [1, 3, 2, 4].
                            Then, swap arr[1] and arr[2]. The array becomes [1, 2, 3, 4], which is sorted.
            Input: arr = [4, 3, 1, 2]
            Output: false
            Explanation: It is not possible to sort the array with exactly two swaps.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ arr.size()
"""

class Solution:
    def checkSorted(self, arr):
        swap = 0
        sorted_arr = sorted(arr)
        for index in range(len(arr)):
            j = index+1
            flag = 1
            while arr[j-1]!=index+1:
                j = arr[j-1]
                if flag:
                    flag = 0
                    swap += 1
            arr[index], arr[j-1] = arr[j-1], arr[index]
            if arr==sorted_arr or swap>2:
                break
        return swap==0 or swap==2
    

# ------- Driver code of geekforgeeks -----------
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr = list(map(int, input().split()))
        sol = Solution()
        result = sol.checkSorted(arr)
        if result:
            print("true")
        else:
            print("false")