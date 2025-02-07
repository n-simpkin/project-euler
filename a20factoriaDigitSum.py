factorial = 1
ans = 0
for i in range(1,101):
  factorial*=i
print(factorial)
factorialSum = [int(i) for i in str(factorial)] 
print(factorialSum)
for num in factorialSum:
  ans += num
print(ans)