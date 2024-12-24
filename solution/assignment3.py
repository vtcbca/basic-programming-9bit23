def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

terms = int(input("Enter the number of terms: "))
fib_seq = list(fibonacci_generator(terms))
print(f"Fibonacci sequence with {terms} terms: {fib_seq}")
