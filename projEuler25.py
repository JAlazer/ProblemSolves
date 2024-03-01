# 1000-digit Fib Number

x = 1
y = 1
c = 2
big = [x, y, c]
switch = True
while switch:
    x = y
    y = c
    c = x + y
    big.append(c)
    if len(str(c)) == 1000:
        switch = False
print(len(big))

