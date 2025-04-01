from EulerLibrary import findDivisors

#New, going for a fully like top down plan type approach before coding.
#Aka unedrstanding the problem polya
for i in range(1,21):
    print(i, 1/i)

#Put in big loop
numsToCheck = []
if num % 5 == 0 and num % 2 == 0:
    if set(findDivisors(num)) == {2, 5}:
        numsToCheck.append(num)

#If denominator can be written in the form 2^n5^m, it won't have a repeating cycle. otherwise, has repeating cycle. Therefore solves problem of how much of the decimal to store, as just keep increasing until cycle is found.
for num in range(7,8):
    decimal = 1/num
    lastSeen = dict()
    for currentDigitPosition in range(20): #TEMP
        digit = int(((decimal*(10**(currentDigitPosition))) - int(decimal*(10**(currentDigitPosition)))) * 10) #Plus one so we don't check int(decimal*1) which will be the starting zero and is not part of the sequence.
        print(digit)
        if digit in lastSeen: #If same, possibly the start of a repeating cycle.
            lastInstanceOfCurrentDigit = lastSeen[digit]
            numDigitsToCheck = currentDigitPosition - lastInstanceOfCurrentDigit #neccessary?
            #Reconstruct the decimals between these digits
            digitsAfter = ""
            for subsequentDigitPosition in range((currentDigitPosition + 1), ((currentDigitPosition + 1) + numDigitsToCheck)): #plus ones so checking next digit, as the start is inclusive.
                digitsAfter += str(int(((decimal*(10**(currentDigitPosition))) - int(decimal*(10**(currentDigitPosition)))) * 10))
            digitsBefore = ""
            for prevRepeatingSection in range((lastInstanceOfCurrentDigit + 1), ((lastInstanceOfCurrentDigit + 1) + numDigitsToCheck)): #plus ones so checking next digit, as the start is inclusive.
                digitsBefore += str(int(((decimal*(10**(lastInstanceOfCurrentDigit))) - int(decimal*(10**(lastInstanceOfCurrentDigit)))) * 10))
        lastSeen[digit] = currentDigitPosition

print(lastSeen)

        
