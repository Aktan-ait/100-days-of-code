def is_valid_parentheses(s):
    stack = []
    for c in s:
        if c in '([{': stack.append(c)
        elif c in ')]}':
            if not stack or (c == ')' and stack[-1] != '(') or (c == ']' and stack[-1] != '[') or (c == '}' and stack[-1] != '{'):
                return False
            stack.pop()
    return not stack

s = input("Скобки: ")
print(is_valid_parentheses(s))
