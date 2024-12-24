def is_prime_while_loop(n):
    if n <= 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

number = int(input("Enter a number: "))
if is_prime_while_loop(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
