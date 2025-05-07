from EulerLibrary import findDivisors
import numpy as np

def getNextDigitOfDecimal(decimal, currentDigitPosition):
    nextDigit = int(((decimal*(10**(currentDigitPosition))) - int(decimal*(10**(currentDigitPosition)))) * 10) #Plus one so we don't check int(decimal*1) which will be the starting zero and is not part of the sequence.
    return nextDigit

#New, going for a fully like top down plan type approach before coding.
#Aka understanding the problem polya
for i in range(1,21):
    print(i, 1/i)

# #Put in big loop
# numsToCheck = []

# for num in range (1,1000):
#     if num % 5 == 0 or num % 2 == 0: #5 & 0 automatically caught
#         divisors = set(findDivisors(num)) 
#         if divisors == {2,5} or divisors == {2} or divisors == {5}:
#             numsToCheck.append(num)
    
#Quicker to generate the numbers?

#2^9, 5^4 for the specific powers.
numsExclude = set()

for i in range(10): #Could narrow my ranges more probably but can't be bothered.
    for j in range(5):
        num = (2**i) * (5**j)
        if num < 1000:
            numsExclude.add(num)

print("excl", numsExclude)
numsCheck = set([i for i in range(1,1000)])
numsCheck -= numsExclude
print(numsCheck)

#If denominator can be written in the form 2^n5^m, it won't have a repeating cycle. otherwise, has repeating cycle. Therefore solves problem of how much of the decimal to store, as just keep increasing until cycle is found.
for num in range(7,8):
    decimal = 1/num
    lastSeen = dict()
    for currentDigitPosition in range(20): #TEMP
        #Get next digit:
        #digit = int(((decimal*(10**(currentDigitPosition))) - int(decimal*(10**(currentDigitPosition)))) * 10) #Plus one so we don't check int(decimal*1) which will be the starting zero and is not part of the sequence.
        digit = getNextDigitOfDecimal(decimal, currentDigitPosition)
        print(digit)

        if digit in lastSeen: #If same, possibly the start of a repeating cycle.
            lastInstanceOfCurrentDigit = lastSeen[digit]
            numDigitsToCheck = currentDigitPosition - lastInstanceOfCurrentDigit #neccessary?
            #Reconstruct the decimals between these digits

            #String concatenation not efficient
            digitsAfter = ""
            for subsequentDigitPosition in range((currentDigitPosition + 1), ((currentDigitPosition + 1) + numDigitsToCheck)): #plus ones so checking next digit, as the start is inclusive.
                digitsAfter += str(int(((decimal*(10**(currentDigitPosition))) - int(decimal*(10**(currentDigitPosition)))) * 10))
            digitsBefore = ""
            for prevRepeatingSection in range((lastInstanceOfCurrentDigit + 1), ((lastInstanceOfCurrentDigit + 1) + numDigitsToCheck)): #plus ones so checking next digit, as the start is inclusive.
                digitsBefore += str(int(((decimal*(10**(lastInstanceOfCurrentDigit))) - int(decimal*(10**(lastInstanceOfCurrentDigit)))) * 10))
        
        lastSeen[digit] = currentDigitPosition

print(lastSeen)

        
