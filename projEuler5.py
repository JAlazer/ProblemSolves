# Smallest Multiple
#******* Proj Euler forums
import time
start = time.time()
x = 1

#GCD
for i in range(1, 21):
    if x % i != 0:

        #LCM
        for j in range(1, 21):
            y = x * j
            if y % i == 0:
                x *= j
                break
print(x)

end = time.time()
run = end - start
print(run)

