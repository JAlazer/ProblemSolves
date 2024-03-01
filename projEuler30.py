# Digi Fifth Power

myList = []

for a in range(10):
    for b in range(10):
        first_sum = a ** 5 + b ** 5
        if str(first_sum) == str(a) + str(b):
            myList.append(first_sum)
        for c in range(10):
            second_sum = a ** 5 + b ** 5 + c ** 5
            if str(second_sum) == str(a) + str(b) + str(c):
                myList.append(second_sum)
            for d in range(10):
                third_sum = a ** 5 + b ** 5 + c ** 5 + d ** 5
                if str(third_sum) == str(a) + str(b) + str(c) + str(d):
                    myList.append(third_sum)
                for e in range(10):
                    fourth_sum = a**5 + b**5 + c**5 + d**5 + e**5
                    if str(fourth_sum) == str(a) + str(b) + str(c) + str(d) + str(e):
                        myList.append(fourth_sum)
                    for f in range(10):
                        fifth_sum = a**5 + b**5 + c**5 + d**5 + e**5 + f**5
                        if str(fifth_sum) == str(a)+str(b)+str(c)+str(d)+str(e)+str(f):
                            myList.append(fifth_sum)
print(myList)
print(sum(myList))
