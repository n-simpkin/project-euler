from EulerLibrary import computePascal

triangle = computePascal(39)
lattice = triangle[:20]
paths = 1
num = 1

for row in range(20,39): #trims triangle into a lattice
  triangle[row] = triangle[row][num:-num]
  lattice.append(triangle[row])
  num +=1

for row in lattice:
  print(row)
for row in lattice:
  for num in row:
    paths += num
print(paths)
