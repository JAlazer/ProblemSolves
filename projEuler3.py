# Prime Factorization
import time
start = time.time()

switch = True
x = 0
y = 13195
while switch:
    x += 1
    divi = y % x
    if divi == 0:
        y = y / x
        print(y , '/', x)
    if x > y:
        switch = False
print("Largest Prime Factor:", x)

end = time.time()
run = end - start
print(run)

