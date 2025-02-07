from math import sqrt

a = 0
b = 0
c = 0
found = False
while found == False and b < 1000:
  b += 1
  while found == False and a < 1000:
    a += 1
    c = sqrt((a**2) + (b**2))
    if c % 1 == 0:
      if a+b+c == 1000.0:
        print("found",a,b,c)
        print(a*b*c)
        found = True
  a = 0