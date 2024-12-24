def is_palindrome_stack(s):
    stack = list(s)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return s == reversed_str

string = input("Enter a string: ")
if is_palindrome_stack(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
