numNames = {
  "0": "",
  "00": "",
  "1": "one",
  "2": "two",
  "3": "three",
  "4": "four",
  "5": "five",
  "6": "six",
  "7": "seven",
  "8": "eight",
  "9": "nine",
  "10": "ten",
  "11": "eleven",
  "12": "twelve",
  "13": "thirteen",
  "14": "fourteen",
  "15": "fifteen",
  "16": "sixteen",
  "17": "seventeen",
  "18": "eighteen",
  "19": "nineteen",
  "20": "twenty",
  "30": "thirty",
  "40": "forty",
  "50": "fifty",
  "60": "sixty",
  "70": "seventy",
  "80": "eighty",
  "90": "ninety",
  "100": "hundred",
  "1000": "thousand"
}

wordLengths = 0

for num in range(1, 1001):
  tens = False
  lastzero = False
  num = str(num)
  #print("num:",num)
  num = [digit for digit in num]
  #print(num)
  #if 1000
  if len(num) == 4:
    wordLengths += len(numNames["1"] + numNames["1000"])
  #if in 100s
  elif len(num) == 3:
    wordLengths += len(numNames[num[0]]) + len(numNames["100"]) 
    #print(numNames[num[0]] + numNames["100"],end = "")
    if num[-2] + num[-1] != "00":
      wordLengths += len("and")
      #print("and")
  if len(num) == 2 or len(num) == 3:
    #handle the teen numbers
    if num[-2] == "1" and num[-1] != "0":
      wordLengths += len(numNames[num[-2] + num[-1]])
      #print(numNames[num[-2] + num[-1]])
      tens = True
    else:
      wordLengths += len(numNames[num[-2] + "0"])
      #print(numNames[num[-2] + "0"])
  #does the last digit
  if tens == False:
    wordLengths += len(numNames[num[-1]])
    #print(numNames[num[-1]])
  #print(wordLengths)
print(wordLengths)