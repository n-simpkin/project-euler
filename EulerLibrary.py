def findHighestPrimeFactor(n):
  pFactors = []
  f = 2
  if n % f == 0:
    pFactors.append(f)
    while n % f == 0:
      n //= f
  f = 1
  while n != 1:
    f += 2
    if n % f == 0:
      pFactors.append(f)
      while n % f == 0:
        n //= f
  return f


lcmList = []


#This alg sucks so bad
def findLcm(multiplesList):
  if len(multiplesList) % 2 == 0 and len(
      multiplesList) != 2:  #splits list into pairs of values
    for i in range(len(multiplesList) - 1):
      print("finding lcm of", multiplesList[i:i + 2])
      findLcm(multiplesList[i:i + 2])
    for i in range(len(lcmList) - 1):
      print("finding lcm of", lcmList[0:2], "from lcm list")
      findLcm(lcmList[0:2])
  elif len(multiplesList) != 1:
    hcf = max(multiplesList)
    found = False
    worksFor = 0
    while found == False:  #Finds hcf
      for item in multiplesList:
        if item % hcf != 0:
          hcf -= 1
          worksFor = 0
        else:
          worksFor += 1
          # print(hcf, "works for",item, "works for =", worksFor)
          # print(len(multiplesList))
          if worksFor == len(multiplesList):
            found = True

    #print("hcf is",hcf)
    product = 0
    #print(multiplesList)
    product = multiplesList[0] * multiplesList[1]
    if type(multiplesList[0]) != float:
      lcmList.append(product / hcf)
    else:
      #print("product =", product)
      del lcmList[0:2]
      lcmList.insert(0, product / hcf)
    #print("lcm is",product/hcf)
    print("lcm list is", lcmList)
    # print("lcm list len", len(lcmList))
    # print(lcmList[0])
  if len(lcmList) == 1:
    return lcmList[0]


#probably not the most efficient but hey
def isPrime(num):
  if num > 1:
    for divisor in range(2, int(num**0.5) + 1):
      if num % divisor == 0:
        return False
    return True
  return False


def mergeSort(unsortedList):  #doesnt work
  splitList = []
  for split in range(0, len(unsortedList), 2):
    splitList.append(unsortedList[split:split + 2])
  for item in splitList:  #sort twos
    item[0], item[1] = min(item), max(item)
  for merge in range(len(splitList) // 2):
    splitList.insert(0, [])
    if splitList[merge][0] < splitList[merge + 1][0]:
      splitList[0].append(splitList[merge][0])
    else:
      splitList[0].append(splitList[merge + 1][0])
  print(splitList)


def findDivisors(num):
  divisors = []
  for divisor in range(1, int(num**0.5) + 1):
    if num % divisor == 0:
      divisors.append(divisor)
      divisors.append(int(num / divisor))
  return divisors


def computePascal(upToRow):
  triangle = [[1], [1, 1], [1, 2, 1]]
  for row in range(3, upToRow):
    currentRow = []
    for num in range(0, row - 1):
      if num == 0:
        currentRow.append(1)
        currentRow.append(triangle[row - 1][num] + triangle[row - 1][num + 1])
      else:
        currentRow.append(triangle[row - 1][num] + triangle[row - 1][num + 1])
    currentRow.append(1)
    triangle.append(currentRow)
  return(triangle)