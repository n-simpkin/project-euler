prevFib = 1
fib = 2
total = 0
while fib < 4000000:
  if fib % 2 == 0:
    total += fib
  prevFib, fib = fib, prevFib + fib
print(total)