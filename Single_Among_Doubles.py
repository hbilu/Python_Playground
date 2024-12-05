"""
Given a sorted array arr[] of n positive integers having all the numbers occurring exactly twice,
except for one number which will occur only once. Find the number occurring only once.

Examples :  Input: n = 5, arr[] = {1, 1, 2, 5, 5}
            Output: 2
            Explanation: Since 2 occurs once, while other numbers occur twice, 2 is the answer.

Expected Time Complexity: O( Log(n) ).
Expected Auxiliary Space: O(1).

Constraints
0 <  n  <= 10^6
0 <= arr[i] <= 10^9

"""

# first way: binary search - time complexity O(logn), space complexity O(n)
class Solution:
    def search(self, n, arr):
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            # In a sorted array, if mid is the unique number, it will not have matching adjacent pairs
            if mid % 2 == 0:
                # If mid is even, check if mid and mid+1 are the same
                if arr[mid] == arr[mid + 1]:
                    left = mid + 2  # Unique number lies in the right half
                else:
                    right = mid  # Unique number lies in the left half
            else:
                # If mid is odd, check if mid and mid-1 are the same
                if arr[mid] == arr[mid - 1]:
                    left = mid + 1  # Unique number lies in the right half
                else:
                    right = mid - 1  # Unique number lies in the left half
        # After exiting the loop, 'left' and 'right' should point to the same number, the unique number
        return arr[left]

# second way: time complexity O(n), space complexity O(n) - (but also accepted by geekforgeeks as solution)
class Solution:
    def search(self, n, arr):
        hashmap = {}
        for i in range(n):
            if arr[i] in hashmap:
                hashmap[arr[i]] += 1
            else:
                hashmap[arr[i]] = 1
        for key, value in hashmap.items():
            if value == 1:
                return key

# third way: using Python Counter - time and space complexity O(n) - (but also accepted by geekforgeeks as solution)
class Solution:
    def search(self, n, arr):
        from collections import Counter
        Dic=Counter(arr)
        for i in Dic.keys():
            if Dic[i]==1:
                return i

# fourth way: time and space complexity O(n) - (but also accepted by geekforgeeks as solution)
# In the worst case, the loop runs n//2 times because we increment i by 2 in each iteration.
# But, n//2 grows at the same rate as n: that is, when n doubles, the number of loop iterations also roughly doubles.
class Solution:
    def search(self, n, arr):
        i = 0
        while i<n-1:
            if arr[i] == arr[i+1]:
                i+=2
            else:
                return arr[i]
        # if not found, last number is unique
        return arr[i]

# ------- Driver code of geekforgeeks -----------
if __name__ == "__main__":
    t = int(input())
    for tc in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.search(n, arr))
        print("~")