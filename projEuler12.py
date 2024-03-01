# Highest Divisible Triangular Number
import math
import time
start = time.time()
sum = 0
counter = 0
x = 0
switch = True
while switch:
    counter += 1
    sum = sum + counter
    sqrt = sum ** .5
    for j in range(math.floor(sqrt), 0, -1):
        if sum % j == 0:
            x += 1
            print(j, "#", x)
        if x > 249:
            print(sum)
            switch = False
            break
    x = 0
end = time.time()
run = end - start
print(run)

