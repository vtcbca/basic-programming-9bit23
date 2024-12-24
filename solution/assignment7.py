def print_triangle_list_comprehension(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        numbers = " ".join([str(x) for x in range(1, 2 * i)])
        print(spaces + numbers)

n = int(input("Enter the number of rows: "))
print_triangle_list_comprehension(n)
