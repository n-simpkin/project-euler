numsAsFile = open("./a13largeSum.txt", "r")
numsAsText = numsAsFile.read()
total = 0
for line in range(0,5000,50):
  total += int(numsAsText[line:line+50])
print(total)