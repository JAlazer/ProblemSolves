# Palindrome Effect
import time
start = time.time()

max = 1000
interval = 100

x = 0
high_x = 0
for i in range(max-interval, max):
    for j in range(max-interval, max):
        x = i * j
        x_str = str(x)
        if x_str[:len(x_str)//2] == x_str[-1:len(x_str)//2*-1-1:-1]:
            if x > high_x:
                high_x = x
print(high_x)

end = time.time()
run = end - start
print(run)

