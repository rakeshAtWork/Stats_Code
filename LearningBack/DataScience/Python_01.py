def print_pattern(n):
    for i in range(1, n + 1):
        spaces = abs(i - (n // 2 + 1))
        stars = n - 2 * spaces
        print(" " * spaces + "*" * stars)
        
print_pattern(5)