import time
start = time.time()

x = 1
y = 2
c = x + y
f_list = [y]
for i in range(101):
    x = y
    y = c
    c = x + y
    if c % 2 == 0 and c <= 4000000:
        f_list.append(c)

print(sum(f_list))
print(f_list)

end = time.time()
run = end - start
print(run)

