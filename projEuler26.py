# reciprocal cycles
import math

cycles = []

for i in range(2, 1000):
    x = 1/i
    if len(str(x)) > 20:
        if str(x)[4:4+8] == str(x)[4+8:4+8+8]:
            cycles.append(x+i)

print(cycles)


