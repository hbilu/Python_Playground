"""
You are given an array arr[] of size n. Find the total count of sub-arrays having their sum equal to 0.

Example:    Input: n = 6, arr[] = {0,0,5,5,0,0}
            Output: 6
            Explanation: The 6 subarrays are [0], [0], [0], [0], [0,0], and [0,0].
Example:    Input: n = 10, arr[] = {6,-1,-3,4,-2,2,4,6,-12,-7}
            Output: 4
            Explanation: The 4 subarrays are [-1 -3 4] [-2 2], [2 4 6 -12], and [-1 -3 4 -2 2]

Expected Time Complexity: O(n*log(n))
Expected Auxilliary Space: O(n)

Constraints:
1 <= n <= 10^6
-10^9 <= arr[ i ] <= 10^9
"""

class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        hmap = {}
        sum = 0
        # hmap will hold prefix sum count -> arr[0,0,5,5,0,0] -> prefix sum [0,0,5,10,10,10]
        # -> hmap{0:2,5:1,10:3}
        for i in range(n):
            sum += arr[i]
            if sum not in hmap:
                hmap[sum] = 1
            else:
                hmap[sum] += 1
        answer = 0
        # for n legth array, total number of sub arrays = n*(n+1)/2
        # if n>0, one subarray is exluded, (n-1)*(n-1+1)/2, n*(n-1)/2
        # sum = 0 is asked on the question, so for 0, one subarray is not exluded.
        for k, v in hmap.items():
            if k==0:
                answer += int((v*(v+1))/2)
            else:
                answer += int((v*(v-1))/2)
        # answer=6 [0][0][0,0][0][0][0,0]
        return answer