def is_balanced(parentheses):
    stack = []
    for char in parentheses:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:  # Stack is empty
                return False
            stack.pop()
    return len(stack) == 0  # Balanced if stack is empty

# Test the function
test1 = "(()())"
test2 = "(()"
print("Is", test1, "balanced?", is_balanced(test1))  # Output: Is (()) balanced? True
print("Is", test2, "balanced?", is_balanced(test2))  # Output: Is (() balanced? False