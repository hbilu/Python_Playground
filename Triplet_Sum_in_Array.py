"""
Given an array arr[] and an integer target, determine if there exists a triplet in the array
whose sum equals the given target.

Return true if such a triplet exists, otherwise, return false.

Examples:   Input: arr[] = [1, 4, 45, 6, 10, 8], target = 13
            Output: true
            Explanation: The triplet {1, 4, 8} sums up to 13

            Input: arr[] = [1, 2, 4, 3, 6, 7], target = 10
            Output: true
            Explanation: The triplets {1, 3, 6} and {1, 2, 7} both sum to 10.

            Input: arr[] = [40, 20, 10, 3, 6, 7], target = 24
            Output: false
            Explanation: No triplet in the array sums to 24

Constraints:
3 ≤ arr.size() ≤ 103
1 ≤ arr[i] ≤ 105

"""

# with two-pointer technique -> time complexity O(n^2), space complexity O(1)
class Solution:
    def hasTripletSum(self, arr, target):
        arr.sort()  # Sort the array
        n = len(arr)
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                curr_sum = arr[i] + arr[left] + arr[right]
                if curr_sum == target:
                    return True
                # If the current sum is greater than the target, move the right pointer to the left
                elif curr_sum > target:
                    right -= 1
                # If the current sum is less than the target, move the left pointer to the right
                else:
                    left += 1
        return False

# ------- Driver code of geekforgeeks -----------
if __name__ == '__main__':
    tc = int(input().strip())  # Number of test cases
    while tc > 0:
        arr = list(map(int, input().strip().split()))  # Read array
        target = int(input().strip())  # Read the target sum
        ob = Solution()
        print("true"
              if ob.hasTripletSum(arr, target) else "false")  # Output result
        tc -= 1