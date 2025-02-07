from EulerLibrary import isPrime

testNum = 1
primesFound = 1
while primesFound < 10002:
  if isPrime(testNum) == True:
    #print(testNum, "is ", primesFound, "prime")
    primesFound += 1
  testNum += 1
print(testNum - 1)