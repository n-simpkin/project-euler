prevFib = 1
fib = 2
index = 3
while len(str(fib)) < 1000:
  prevFib, fib = fib, prevFib + fib
  index += 1

print(index)