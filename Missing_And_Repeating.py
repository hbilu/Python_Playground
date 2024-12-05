"""
Given an unsorted array arr of positive integers. One number a from the set [1, 2,....,n] is missing
and one number b occurs twice in the array. Find numbers a and b.

Note: The test cases are generated such that there always exists one missing
and one repeating number within the range [1,n].

Examples:   Input: arr[] = [2, 2]
            Output: [2, 1]
            Explanation: Repeating number is 2 and smallest positive missing number is 1.

            Input: arr[] = [1, 3, 3]
            Output: [3, 2]
            Explanation: Repeating number is 3 and smallest positive missing number is 2.

Constraints:
2 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ arr.size()
"""
# first way:
class Solution:
    def findTwoElement( self,arr):
        n = len(arr)
        seen = set()
        duplicate = -1
        # Find the duplicate number
        for num in arr:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)
        # Find the missing number
        missing = -1
        for i in range(1, n+1):
            if i not in seen:
                missing = i
                break
        return [duplicate, missing]

# second way:
class Solution:
    def findTwoElement(self,arr):
        n = len(arr)
        # Calculate the expected sum and sum of squares without missing and duplicated numbers
        sum_expected = n * (n + 1) // 2
        square_expected = n * (n + 1) * (2 * n + 1) // 6
        sum_actual = 0
        square_actual = 0
        # Calculate the actual sum and sum of squares
        for num in arr:
            sum_actual += num
            square_actual += num * num
        # Find the difference between expected and actual sums
        sum_diff = sum_actual - sum_expected  # b - a, where b is the repeated number and a is the missing number.
        square_diff = square_actual - square_expected  # b^2 - a^2,  which we can factor as (b - a)(b + a)
        # From sum_diff = b - a, we can compute b + a
        sum_plus = square_diff // sum_diff  # b + a
        # Now we have the system of equations:
        # b - a = sum_diff
        # b + a = sum_plus
        # Solving for b and a:
        b = (sum_diff + sum_plus) // 2
        a = sum_plus - b
        return [b, a]

# ------- Driver code of geekforgeeks -----------
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1
        print("~")