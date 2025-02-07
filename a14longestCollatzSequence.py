sequenceLen = 0
longestSequenceLen = 0
longestSequenceNum = 0
num = 1
for num in range(1,1000001):
  orgNum = num
  while num > 1:
    if num % 2 == 0: #if even
      num = num/2
    else:
      num = 3 * num + 1
    sequenceLen += 1
  if num == 1:
    sequenceLen += 1
  if sequenceLen > longestSequenceLen:
    longestSequenceLen = sequenceLen
    longestSequenceNum = orgNum
  sequenceLen = 0
print(longestSequenceLen)
print(longestSequenceNum)