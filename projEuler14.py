# Longest Collatz Sequence
import time
start = time.time()


def collatz_Counter(n):
    term_counter = 1
    o = n
    while True:
        if o == 1:
            if term_counter > 500:
                print(n, "#", term_counter)
            break
        if o % 2 == 0:
            o = o/2
            term_counter += 1
        else:
            o = 3 * o + 1
            term_counter += 1


x = 999999
while x > 0:
    y = x
    collatz_Counter(y)
    x -= 1


end = time.time()
run = end - start
print(run)
