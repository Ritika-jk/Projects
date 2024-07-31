def fibonacci_iterative(n):
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  else:
    fib_sequence = [0, 1]
    for i in range(2, n):
      next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
      fib_sequence.append(next_fib)
    return fib_sequence

num_terms = int(input("enter the number of terms for the series "))
result = fibonacci_iterative(num_terms)
print(result)
