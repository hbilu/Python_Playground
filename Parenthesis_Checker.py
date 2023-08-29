"""
Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

"""

def ispar(self, x):
    stack = []
    for char in x:
        if char in ('(', '{', '['):
            stack.append(char)
        else:
            if stack and ((stack[-1] == '(' and char == ')') or
                          (stack[-1] == '{' and char == '}') or
                          (stack[-1] == '[' and char == ']')):
                stack.pop()
            else:
                return False
    # to check the strings with only one open character like "(open", "op[en" and "open{"
    if not stack:
        return True