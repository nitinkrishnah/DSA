# https://leetcode.com/problems/valid-parentheses/

# Declare a dictionary of opening brackets as keys and closing brackets as values
# declare an empty stack
# loop through the string 
#     if character is opening bracket, the append the stack
#     if character is closing bracket, 
#         False if stack is empty or the item in stack is not matching the closing bracket

# Finally after all characters in string, if the stack is empty, returm true

def isValid(s) :
        stack = []
        brackets = {'(':')', '{':'}', '[':']'}

        for char in s:
            if char in brackets:
                stack.append(char)
            elif len(stack) == 0 or brackets[stack.pop()] != char:
                return False
        return len(stack) == 0

print((isValid("()[]{}")))