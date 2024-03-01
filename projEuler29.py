# Distinct Powers
dif_term = []

for a in range(2, 101):
    for i in range(2, 101):
        distinct = a ** i
        if distinct not in dif_term:
            dif_term.append(distinct)
dif_term.sort()
print(len(dif_term))

