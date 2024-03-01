# Summation of primes
import time
import math
start = time.time()


num = 2000000
sum = 0
for numbers in range(num, 1, -1):
    divisor_count = 1
    sq_num = numbers ** 0.5
    for i in range(2, math.floor(sq_num) + 1):
        if numbers % i == 0:
            divisor_count += 1
            break
    if divisor_count == 1:
        sum = numbers + sum
print("Sum:", sum)


end = time.time()
runtime = end - start
print(runtime)
