from EulerLibrary import findDivisors

amicableNums = set()

for num in range(1, 10000):
  # print(num)
  sumOfNumDivisors = 0
  maybeNum = 0
  for i in findDivisors(num):
    if int(i) != num:
      sumOfNumDivisors += int(i)
  # print(sumOfNumDivisors)
  for i in findDivisors(sumOfNumDivisors):
    if int(i) != sumOfNumDivisors:
      maybeNum += int(i)
  # print(maybeNum)
  if maybeNum == num:
    if sumOfNumDivisors != num:
      print(sumOfNumDivisors, maybeNum)
      amicableNums.add(sumOfNumDivisors)
      amicableNums.add(maybeNum)
    
ans = 0
for num in amicableNums:
  ans += num

print(ans)