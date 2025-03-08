def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

num_terms = int(input("Enter the number of Fibonacci terms: "))
print("Fibonacci Series:")
for num in fibonacci_generator(num_terms):
    print(num)
