def print_pattern_list_comprehension(n):
    for i in range(1, n + 1):
        # Create the row using list comprehension for increasing and decreasing letters
        row = " " * (n - i) + " ".join([chr(64 + j) for j in range(1, i + 1)]) + " ".join([chr(64 + j) for j in range(i - 1, 0, -1)])
        print(row)

n = int(input("Enter the number of rows: "))
print_pattern_list_comprehension(n)
