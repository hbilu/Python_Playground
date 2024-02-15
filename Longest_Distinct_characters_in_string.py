"""
Given a string S, find the length of the longest substring with all distinct characters.

Example: Input: S = "geeksforgeeks"
         Output: 7
         Explanation: "eksforg" is the longest substring with all distinct characters.

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(K), where K is Constant.

Constraints:
1<=|S|<=105
"""
class Solution:

    def longestSubstrDistinctChars(self, S):
        if len(set(S)) == len(S): return len(S)
        i = 0
        j = 1
        maxlen = 0
        while j<len(S)+1:
            strx = S[i:j]
            lenx = len(strx)
            if lenx == len(set(strx)):
                j += 1
                if lenx>maxlen:
                    maxlen=lenx
            else:
                i += 1
        return maxlen

# second way

class Solution:
    def longestSubstrDistinctChars(self, S):
        last_idx = {}
        max_len = 0
        start_idx = 0
        for i in range(0, len(S)):
            if S[i] in last_idx:
                start_idx = max(start_idx, last_idx[S[i]] + 1)
                # print("start", start_idx)
            max_len = max(max_len, i-start_idx + 1)
            # print("max", max_len)
            last_idx[S[i]] = i
        return max_len