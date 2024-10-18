"""
Given an array arr. Your task is to find the elements whose value is equal to that of its index value
( Consider 1-based indexing ).

Examples:       Input: arr[] = [15, 2, 45, 4 , 7]
                Output: 2 , 4
                Explanation: Here, arr[2] = 2 exists here. and arr[4] = 4 exists here.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(k)

Constraints:
1 ≤ arr.size ≤ 105
1 ≤ arr[i] ≤ 106
"""

class Solution:
    # Function to find values in array equal to their indices
    def valueEqualToIndex(self, arr):
        result=[]
        for index in range(0,len(arr)):
            if index+1 == arr[index]:
                result.append(index+1)
        return result

# ------- Driver code of geekforgeeks -----------
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.valueEqualToIndex(arr)
        if len(ans) == 0:
            print("Not Found")
        else:
            for x in ans:
                print(x, end=" ")
            print()
        tc -= 1
