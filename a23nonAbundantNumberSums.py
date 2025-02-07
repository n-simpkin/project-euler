from EulerLibrary import findDivisors

abundantNumbers = []
sumOfAbundantNumbersNums = set()

for num in range(1, 28124):  #Find abundant numbers - works
  # print("num is", num)
  divisorSum = 0
  divsList = set(findDivisors(num)) #eliminating duplicates
  for divisor in divsList:
    # if divisor != num and divisor != sqrt(num):
    if divisor != num: #removes duplicate nums
      # print("divisor", divisor)
      divisorSum += divisor
  # print("div sum", divisorSum)
  if divisorSum > num:
    abundantNumbers.append(num)
    # print("is abundant")
  # if num % 1000 == 0:
    # print(num)
  # print("\n")
# print(abundantNumbers)

#Generate abundant number sums
for abundant in abundantNumbers:
  for abundant2 in abundantNumbers:
    sum = abundant + abundant2
    sumOfAbundantNumbersNums.add(sum)

numbers = set(range(1, 28124))
nonAbundantSum = numbers.difference(sumOfAbundantNumbersNums)
# print(sorted(nonAbundantSum))
tot = 0
for num in nonAbundantSum:
  tot += num
print(tot)

#{7621, 1771, 1141}
# from functools import reduce

# def factors(n):    
#   return set(reduce(list.__add__, 
#     ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))
    
# def sumOfFactors(n: int) -> int:
#   fs = factors(n)
#   sum = 0

#   for factor in fs:
#     if factor != n:
#       sum += factor

#   return sum
 
# abundants = [12]

# for i in range(13, 28_124):
#   factorSum = sumOfFactors(i)

#   if factorSum > i:
#     abundants.append(i)

# canBeSumOfAbundants = set()

# for abundant in abundants:
#   for abundant2 in abundants:
#     sum = abundant + abundant2
#     canBeSumOfAbundants.add(sum)

# numbers = set(range(1, 28_124))
# nonAbundant = numbers.difference(canBeSumOfAbundants)
# naSum = 0
# for s in nonAbundant:
#   naSum += s
# print(naSum)

# print(nonAbundantSum.difference(nonAbundant))
# abundantNumbers = set(abundantNumbers)
# abundants = set(abundants)
# for elem in abundantNumbers:
#   if elem not in abundants:
#     print(elem)