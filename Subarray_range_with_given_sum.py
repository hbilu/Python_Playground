"""
Given an unsorted array of integers arr[], and a target tar,
determine the number of subarrays whose elements sum up to the target value.

Examples:   Input: arr[] = [10, 2, -2, -20, 10] , tar = -10
            Output: 3
            Explanation: Subarrays with sum -10 are: [10, 2, -2, -20], [2, -2, -20, 10] and [-20, 10].

            Input: arr[] = [1, 4, 20, 3, 10, 5] , tar = 33
            Output: 1
            Explanation: Subarray with sum 33 is: [20,3,10].

Expected Time Complexity: O(n)
Expected Auxilary Space: O(n)

Constraints:
1 <= arr.size() <= 106
-105 <= arr[i] <= 105
-105 <= tar <= 105
"""

class Solution:
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        curr_sum = {0:1}
        count = 0
        sum = 0
        for i in range(0, len(arr),1):
            sum += arr[i]
            if sum-tar in curr_sum:
                count += curr_sum[sum-tar]
            if sum in curr_sum:
                curr_sum[sum]+=1
            else:
                curr_sum[sum]=1
        return count

# ------- Driver code of geekforgeeks -----------
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar = int(input())
        ob = Solution()
        res = ob.subArraySum(arr, tar)
        print(res)
        # print("~")
        t -= 1
