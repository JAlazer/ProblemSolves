# Non-abundant Sums
import time
start = time.time()


# function to run through factors
def fac_find(n, arr):
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    return arr


perfects = []
nons = []
abundo = []
x = 1

# loop to check if x is a perfect, non-abundant, or abundant number
while x <= 28123:
    # factors
    x_list = []
    fac_find(x, x_list)

    # adds x to appropriate list
    if sum(x_list) == x:
        perfects.append(x)
    elif sum(x_list) < x:
        nons.append(x)
    elif sum(x_list) > x:
        abundo.append(x)

    x += 1

# keeps the sums of the abundant numbers
abundo_sum = []
for j in abundo:
    for k in abundo:
        if j + k <= 28123 and j + k not in abundo_sum:
            abundo_sum.append(j + k)
        if j + k > 28123:
            break


# loop to remove the abundo sums from each list
for a in abundo_sum:
    if a in perfects:
        perfects.remove(a)
    elif a in nons:
        nons.remove(a)
    elif a in abundo:
        abundo.remove(a)
    else:
        print(abundo_sum)

print(sum(perfects) + sum(nons) + sum(abundo))

end = time.time()
print(end - start)
