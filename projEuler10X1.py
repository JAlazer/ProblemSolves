# Summation of primes
import math
import time
start = time.time()


def prime_find(n, my_num):
    divisor_count = 0
    for i in range(2, math.floor(n**.5) + 1):
        if n % i == 0:
            divisor_count += 1
            break
    if divisor_count == 0:
        my_num.append(n)
        return my_num


num_list = []
for j in range(2000000, 1, -1):
    prime_find(j, num_list)

summation = 0
for k in num_list:
    summation = summation + k
print(summation)

end = time.time()
run = end - start
print(run)

