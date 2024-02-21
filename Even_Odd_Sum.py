"""
Given an array Arr[] of N integers.Find the sum of values of even and odd index positions separately.

Example 1:  Input: N=5, Arr={1,2,3,4,5}
            Output: 9 6
            Explanation: The sum of elements at odd places i.e at 1st,3rd and 5th places are (1+3+5=9)
                         Similarly,the sum of elements at even places i.e. at 2nd and 4th places are (2+4=6).

Expected Time Complexity:O(N)
Expected Auxillary Space:O(1)

Constraints:
1<=N<=105
0<=Arr[i]<=104,for 0<=i
"""

#first way
class Solution:
    def EvenOddSum(self,N,Arr):
        esum = 0
        osum = 0
        for i in range(0,N):
            if i%2 == 0:
                osum += Arr[i] #even index indicates odd number
            else:
                esum += Arr[i]
        return esum, osum

#second way
class Solution:
    def EvenOddSum(self,N,Arr):
        return sum(Arr[i] for i in range(N) if i%2==0), sum(Arr[i] for i in range(N) if i%2!=0)