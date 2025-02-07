with open("a18maximumSumPathTriangle.txt") as file:
  triangle = [ row.split() for row in file]
print(triangle)

triangleMean = 0
digitCount = 0
#Calculate mean
for row in triangle:
  for digit in row:
    triangleMean += int(digit)
    digitCount += 1
triangleMean /= digitCount

def isWorth(pathSum):
  if pathSum > row * triangleMean:
    return True
  else:
    return False
    
#checks paths
pathSum = 0
row = 0
across = 0
allChecked = False

# while allChecked == False:
#check path
pathSum += int(triangle[0][0])
row += 1
while isWorth(pathSum) == True:
  pathSum += int(triangle[1][0])
  row += 1
print(pathSum)
print(triangleMean)