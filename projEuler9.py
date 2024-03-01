# Special Pythagorean Triplet
import math
import time
start = time.time()


def pythag_count(m, n, switch):
    while switch:
        m_sq = m ** 2
        n_sq = n ** 2
        total = m_sq + n_sq
        sqrt = total ** .5
        if math.floor(sqrt) ** 2 == total:
            sqrt = int(sqrt)
            perfect_total = m + n + sqrt
            if perfect_total == 1000:
                print(m, n, sqrt)
                print(m * n * sqrt)
                return False
        if n > 500:
            return False
        n += 1


x, y = 3, 4
runner_p = True
while x <= 300:
    y += 1
    pythag_count(x, y, runner_p)
    x += 1


end = time.time()
run = end - start
print(run)


