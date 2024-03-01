# Amicable numbers
import time

start = time.time()
x = 10000
sum_z = 0
while x > 0:
    n = x
    factors = n - 1
    sum = 0
    while factors > 0:
        if n % factors == 0:
            sum = factors + sum
        factors -= 1
    sum_factor = sum - 1
    sum_pair = 0
    while sum_factor > 0:
        if sum % sum_factor == 0:
            sum_pair = sum_factor + sum_pair
        sum_factor -= 1
    if sum_pair == n:
        if n != sum:
            switch = True
            while switch:
                sum_z = sum_z + n
                break
    x -= 1
print(sum_z)

end = time.time()
run = end - start
print(run)
