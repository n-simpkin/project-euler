# allRemainders = {}
# for d in range(2,21):
#   print(1/d)
#   # remainderAsString = "{:.40f}".format(1/d)
#   remainderAsString = str(1/d)
#   remainder = [digit for digit in remainderAsString.strip("0.")]
#   # print(remainder)
#   prevPresent = []
#   possibleMatch = []
#   digitIndex = 0
#   found = False

#   while found == False and digitIndex < len(remainder):
#     if remainder[digitIndex] in prevPresent:
#       #the problem is that if a number appears twice in the same reccuring sequence it throws the whole program outta whack
#       possibleMatch.append(remainder[digitIndex])
#       if possibleMatch == prevPresent:
#         # print("Remainder is", possibleMatch)
#         remAsString = "".join(possibleMatch)
#         print("rem is ", remAsString)
#         allRemainders[remAsString] = d
#         found = True
#     else:
#       prevPresent.append(remainder[digitIndex])
#       possibleMatch = []
#     digitIndex += 1

# print(sorted(allRemainders.keys(), key=len)[::-1])
# print(sorted(allRemainders.keys(), key=len)[::-1][0])
# print(allRemainders[sorted(allRemainders.keys(), key=len)[::-1][0]])
# print(1/allRemainders[sorted(allRemainders.keys(), key=len)[::-1][0]])
# print(1/73)
# for key, val in allRemainders.items():
#   if val == 73:
#     print(key)
#     print("trter")
#     #rework alg so it picks up this case

for num in range(1,20):
  print("num:",1/num)
  
#NEW
repetends = dict()
#do it like  long division? picture on phone
for num in range(1,20):
  repetend = []
  repetendFound = False
  n = 1

  while repetendFound == False:
    toBeDiv = n * 10
    # print("num", num)
    # print("toBeDiv", toBeDiv)
    rem = toBeDiv % num
    # print("rem", rem)
    recDigit = toBeDiv // num
    # print("recDig", recDigit)
    if recDigit in repetend: #this is false
      repetendFound = True
      # if repetend
      if repetend[len(repetend) - 1] == 0:
        # print("chop",repetend)
        repetend.pop()
        # print("chopped",repetend)
    else:
      repetend.append(recDigit)
    n = rem
  repetendAsString = [str(i) for i in repetend]
  repetendAsString = "".join(repetendAsString)
  print("calced num:", num, "rep is", repetendAsString)
  repetends[repetendAsString] = num
  # print(repetends)

  #fing largest
print(max(repetends.keys(), key=len))
print(repetends[max(repetends.keys(), key=len)])
print(1 / 86)

#sets
#if digit appears only once it's not part of the reccuring value
#remove any digits that occur only once then if len > 0 ad rest toset which will give the reccuring value
#save to list at end find longest

# from collections import Counter
# reccuringCycles = []

# for d in range(1,11):
#   decimal = [digit for digit in str(1/d).strip("0.")]
#   print(Counter(decimal))
#   print(1/d)
#   for key, val in Counter(decimal).items():
#     if val == 1:
#       decimal.remove(key)
#   if len(decimal) > 0:
#     decimal = set(decimal)
#     # print(decimal)
#     decimal = "".join(decimal)
#     reccuringCycles.append((decimal,d))
#   print(decimal)
# reccuringCycles = dict(reccuringCycles)

# print(reccuringCycles)
# s = sorted(reccuringCycles.keys(), key=len)
# print(s)
# print(s[len(s)-1])
# biggest = s[len(s)-1]
# print(reccuringCycles[biggest])
# print(1/810)
# print(max([dec for dec in reccuringCycles.keys()], key=len))
# print(reccuringCycles[max([dec for dec in reccuringCycles.keys()], key=len)])
# print(reccuringCycles)
# print(max(reccuringCycles, key=len))
# print(max(onlyDec, key=len))
# decimal = set(decimal)
# print(decimal)
