# Factorial digit sum
import math
x = math.factorial(100)
x = str(x)
sum = 0
for i in x:
    y = int(i)
    sum = y + sum
print(sum)


