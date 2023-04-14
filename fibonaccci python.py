def fibonacci(n):
    if n <= 0:
        return "Invalid input! n must be a positive integer."
    f0, f1 = 0, 1
    print(f0, f1, end=' ')
    for i in range(2, n):
        fi = f0 + f1
        print(fi, end=' ')
        f0 = f1
        f1 = fi
    print()
fibonacci(10)
