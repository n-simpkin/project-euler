namesScores = 0

with open("a22names.txt","r") as file:
  names = file.read()
  names = names.replace('"',"")
  names = names.lower()
  names = names.split(",")
  
names = sorted(names)
for namePosition in range(len(names)):
  wordScore = 0
  name = [letter for letter in names[namePosition]]
  for letter in name:
    wordScore += ord(letter) - 96
  namesScores += wordScore*(namePosition+1)
print(namesScores)
print(names[937])