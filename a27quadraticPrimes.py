#n^2+n+41 - 40 primes for 0 <= n <= 39
#n^2-79+1601 90 primes for 0 <= 0 =< 79
#find formula n^2+an+b where -1000 <= a <= 1000 and -1000 <= b <= 1000 that produces max number of primes for consecutive values of n starting with n = 0
#n is positive
#will be greater than 80 primes

from EulerLibrary import isPrime

primesTo1000 = [1]

for num in range(0, 1001):
  if isPrime(num):
    primesTo1000.append(num)
# print(primesTo1000)

# primesTo1000Inv = []
# for num in primesTo1000:
#   primesTo1000Inv.insert(0, num * -1)
# # print(primesTo1000Inv, "\n")
# primesTo1000 = primesTo1000Inv + primesTo1000
print(primesTo1000)

primesTo1000Incl = primesTo1000
primesTo1000Incl.append(1000)
# primesTo1000Incl.insert(0, -1000)
print(primesTo1000Incl)

largestN = 0
# for a in primesTo1000:
#   for b in primesTo1000Incl:
for a in range(-61,-60):
  for b in range(971,972):
    if (a == 61) and (b == 971):
      print("----------reached 61 971")
    n = 0
    quadraticProduct = ((n**2) + (a * n) + b)
    while isPrime(abs(quadraticProduct)):
      n += 1
      quadraticProduct = (n**2 + a * n + b)
      print("qp =", quadraticProduct)
      print(n)
    if n >= largestN:
    # if n > 5:
      largestN = n
      print(a, b, "made", n, "consecutive primes")
      print(a, b, "coeff product = ", abs(a*b))