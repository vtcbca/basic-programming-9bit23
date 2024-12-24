def print_pattern_list_comprehension(rows):
    for i in range(1, rows + 1):
        print(" ".join([ "*" for _ in range(i)]))

rows = int(input("Enter the number of rows: "))
print_pattern_list_comprehension(rows)
