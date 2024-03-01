# Palindrome Effect
import time
start = time.time()

switch = True
x = 99
y = 100
while switch:
    x += 1
    prod = x * y
    prod = str(prod)
    if x == 999:
        x = 99
        y += 1
    if prod[0] == prod[-1] and prod[1] == prod[-2] and prod[2] == prod[-3]:
        if prod[0] == "9" and prod[-1] == "9":
            print("Palindrome bigger!", prod)
    if y == 999:
        switch = False

end = time.time()
run = end - start
print(run)

