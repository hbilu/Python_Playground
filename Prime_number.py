"""
For a given number n check if it is prime or not.
A prime number is a number which is only divisible by 1 and itself.

Examples :
    Input: n = 5                                    Input: n = 25
    Output: 1                                       Output: 0
    Explanation: 5 has 2 factors 1 and 5 only.      Explanation: 25 has 3 factors 1, 5, 25

Your Task:
Your task is to complete the function isPrime() which takes an integer n as input parameters and returns an integer,
1 if n is a prime number or 0 otherwise.

Expected Time Complexity: O(sqrt(n))
Expected Space Complexity: O(1)

"""

class Solution:
    def isPrime (self, N):
        if N <= 1:
            return 0
        for i in range(2, int(N**0.5)+1):
            if (N % i) == 0:
                return 0
        return 1

# ------- Driver code of geekforgeeks -----------
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        print(ob.isPrime(N))