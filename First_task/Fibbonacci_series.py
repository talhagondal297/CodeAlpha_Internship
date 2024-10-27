def fibonacci_generator(n):
    """Generate Fibonacci series up to n terms."""
    a, b = 0, 1
    series = []
    while len(series) < n:
        series.append(a)
        a, b = b, a + b
    return series


num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
fibonacci_series = fibonacci_generator(num_terms)
print("Fibonacci Series:")
print(fibonacci_series)
