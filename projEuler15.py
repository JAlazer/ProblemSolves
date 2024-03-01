# Lattice Paths
import random


lsd = {1: 'R',
       2: 'L'}

# big list to contain all routes
lsl = []
size = []

# add to big list
while True:

    # list to contain direction of routes
    lils = []

    # keep track of directions
    counterR = 0
    counterL = 0

    # Look for Routes
    for j in range(40):
        rando = random.randrange(1, 3)
        lils.append(lsd[rando])
        if rando == 1:
            counterR += 1
        elif rando == 2:
            counterL += 1

        # stops loop to place remaining directions left
        if counterR == 20:
            holdR = len(lils)
            while holdR > len(lils) - counterR:
                lils.append(lsd[2])
                holdR -= 1
            break
        elif counterL == 20:
            holdL = len(lils)
            while holdL > len(lils) - counterL:
                lils.append(lsd[1])
                holdL -= 1
            break

    # make sure no direction is repeated
    if lils not in lsl:

        # adds directions to big list for one route
        lsl.append(lils)

        # keeps track of number of routes
        size.append(len(lsl))

    print(len(lsl))



