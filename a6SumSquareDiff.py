squareSum = 0
squareOfSum = 0
for num in range(1,101):
  squareSum += num**2
  squareOfSum += num
print(squareOfSum**2 - squareSum)