num1 = 999
num2 = 999
found = False
palindromes = []
while num1 > 99 and num2 > 99:
  if str(num1 * num2) == str(num1 * num2)[::-1]:
    palindromes.append(num1 * num2)
  if num2 > 100:
    num2 -= 1
  else:
    num1 -= 1
    num2 = 999
print(max(palindromes))