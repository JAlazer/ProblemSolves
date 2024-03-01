# Lexicographic Permutation
import math

# gonna contain all orders
matrix = []

order = ['0', '1', '2']
x = 1

# to loop through amount of possible permutations
while x <= math.factorial(len(order)):

    # to get the order
    for i in range(len(order)-2):
        y = order[i+1]
        order[i+1] = order[i+2]
        order[i+2] = y
    print(order)

    if order not in matrix:
        matrix.append(order)

    x += 1
print(matrix)




