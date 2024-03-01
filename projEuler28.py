# Diagonal Number Spiral
# array to hold all numbers being summed up
diag = []
int_diag = 1001**2
counter = 1001
minus = 1000

while 0 < counter:
    for i in range(4):
        if int_diag != 1:
            diag.append(int_diag)
            int_diag -= minus
        else:
            diag.append(int_diag)
            break
    counter -= 2
    minus -= 2
print(diag)
print(sum(diag))
