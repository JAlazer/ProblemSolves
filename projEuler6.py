# Sum Square Difference
import time
start = time.time()


switch = True
nat_num = 0
sqsm = 0
smsq = 0
itr = range(1, 101)
while switch:
    nat_num += 1
    sq = nat_num ** 2
    sqsm = sq + sqsm
    if nat_num == 100:
        print(sqsm)
        sm = sum(itr)
        smsq = sm ** 2
        print(smsq)
        switch = False
smdif = smsq - sqsm
print(smsq, "-", sqsm, "=", smdif)


end = time.time()
run = end - start
print(run)

