#New, going for a fully like top down plan type approach before coding.
for i in range(1,21):
    print(i, 1/i)

for num in range(7,8):
    decimal = 1/num
    lastSeen = dict()
    for digitPosition in range(20): #TEMP
        digit = int(((decimal*(10**(digitPosition))) - int(decimal*(10**(digitPosition)))) * 10) #Plus one so we don't check int(decimal*1) which will be the starting zero and is not part of the sequence.
        print(digit)
        if digit in lastSeen:
            prevInstanceLocation = lastSeen[digit]
        lastSeen[digit] = digitPosition

print(lastSeen)

        