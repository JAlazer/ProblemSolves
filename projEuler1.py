# Sum of multiples of 3 and 5
import time
start = time.time()

sum, starter = 0, 1000
while starter >= 0:
    starter -= 1
    if starter % 3 == 0 or starter % 5 == 0:
        sum = starter + sum
print(sum)

end = time.time()
run = end - start
print(run)
