#New, going for a fully like top down plan type approach before coding.
for i in range(1,21):
    print(i, 1/i)

for num in range(1,10):
    cycle = 1/num
    seen = dict()
    digitPosition = -1
    for digit in str(cycle): #divide by 10 every time sort of thing (more efficient than string conversion)
        digitPosition += 1
        if digit in seen:
            prevInstanceLocation = 0
        else:
            seen[digit] = digitPosition


#Could I implement seen as a dictionary so then I don't have to search for the last occurence
test = {2:4, 3:2}
print(test)
test[2] = 5
test[6] = 7
print(test)

        