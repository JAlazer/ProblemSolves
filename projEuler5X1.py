# Smallest multiple
import time
start = time.time()

x = 20
switch = True

# loop to increase x and test for divisibility
while switch:

    # loop for divisibility
    for i in range(1, 21):
        if x % i != 0:
            x += 20
            break
        if i == 20 and x % i == 0:
            switch = False

print(x)

end = time.time()
print(end - start)

