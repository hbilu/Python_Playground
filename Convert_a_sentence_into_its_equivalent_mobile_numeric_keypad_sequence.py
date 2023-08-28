"""
Given a sentence in the form of a string in uppercase, convert it into its equivalent mobile numeric keypad sequence.
Please note there might be spaces in between the words in a sentence and we can print spaces by pressing 0.

Example:
    Input:
    S = "GFG"
    Output: 43334
    Explanation: For 'G' press '4' one time. For 'F' press '3' three times.
"""

def printSequence(self, S):
    num_list = ["2", "22", "222", "3", "33", "333", "4", "44", "444", "5", "55", "555",
                "6", "66", "666", "7", "77", "777", "7777", "8", "88", "888", "9", "99", "999", "9999"]
    result = ""
    for i in range(0, len(S), 1):
        if S[i] == " ":
            result += "0"
        else:
            # subtracting ASCII value of ‘A’ to obtain the position
            position = ord(S[i]) - ord("A")
            result += num_list[position]
    return result