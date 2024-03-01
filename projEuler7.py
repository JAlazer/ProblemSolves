# 10001st prime
import math
import time
start = time.time()

prime_count = 10001
x = 1
for i in range(prime_count, 0, -1):
    switch = True
    while switch:
        fac_counter = 0
        x += 1
        sq_rt = x ** .5
        for j in range(1, math.floor(sq_rt)+1):
            if x % j == 0:
                fac_counter += 1
        if fac_counter == 1:
            #false
            switch = False
print(x)

end = time.time()
run = end - start
print(run)


