def reverse_string_stack(s):
    stack = list(s)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str

string = input("Enter a string: ")
reversed_string = reverse_string_stack(string)
print(f"Reversed string: {reversed_string}")
