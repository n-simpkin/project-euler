from EulerLibrary import findDivisors

found = False
i = 1
triangleNum = 0
while found == False:
  triangleNum += i
  if len(findDivisors(triangleNum)) > 500:
    print(triangleNum)
    found = True
  i += 1