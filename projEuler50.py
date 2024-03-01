# Consecutive Prime Sums
import primeFind
x = 1
prime_ls = []
spls = []
sume = 0

while x <= 1000:
    point = primeFind.PrimeFind(x)
    check = point.factor()
    if check:
        sume += x
        prime_ls.append(x)
    sum_prime = primeFind.PrimeFind(sume)
    if sum_prime.factor():
        spls.append(sume)
    if sume >= 1000:
        sume -= prime_ls[-1]
        prime_ls.pop(-1)
        break
    x += 1


print(prime_ls)
print(len(prime_ls))
print(sum(prime_ls))
print(spls)
print(sume)










