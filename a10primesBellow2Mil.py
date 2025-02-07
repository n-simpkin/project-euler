from EulerLibrary import isPrime

sumOfPrimes = 0
for potentialPrime in range(1,2000000):
  if isPrime(potentialPrime):
    sumOfPrimes += potentialPrime
print("sum", sumOfPrimes)
