# Max Sum Path II

mytxt = open('/Users/johan/textFiler/p067_triangle.txt', 'r')
reader = mytxt.read()
pyramid = []

make = 0

# get the numbers into the list
for book in reader:
    try:
        make = int(book)
        pyramid.append(str(make))
    except:
        pass


n_pyramid = []
dubs = []
dif = 0

# get the double digit numbers
for new in pyramid:
    dubs.append(new)
    dif += 1
    if dif % 2 == 0:
        x = int(dubs[0]+dubs[1])
        n_pyramid.append(x)
        dubs = []


# array holding each row of numbers
my_list = []
lisin = []

# represents each row of the pyramid
counter = 1

# organize numbers in rows into arrays
for i in range(len(n_pyramid)):
    lisin.append(n_pyramid[i])

    # when the length of the mini array is equal to counter then we make a new mini array
    if len(lisin) == counter:
        my_list.append(lisin)
        lisin = []
        counter += 1


# hold greatest numbers
greats = []

# hold position of number
placement = []

# loop to get each row
for j in range(len(my_list)):

    # holds the max sum path number
    great = 0

    # holds the greater number of the row in front of the first number that is being tested
    nx_great = 0

    # holds the greater number of the row in front of the second number that is being tested
    nx_great2 = 0

    # checks for any number that repeats
    repeat = 0

    # loop through each row
    for k in range(len(my_list[j])):

        # to be able to get an easy index placement with no complications
        if len(my_list[j]) > 1:

            # to prevent an indexing error
            if j < len(my_list)-1:

                # checks the max path sum of the first number checked in the row behind
                if my_list[j+1][placement[-1]] > my_list[j+1][placement[-1]+1]:
                    nx_great = my_list[j+1][placement[-1]]
                elif my_list[j+1][placement[-1]] < my_list[j+1][placement[-1]+1]:
                    nx_great = my_list[j+1][placement[-1]+1]

                # checks the max sum path of the second number being checked in row behind
                if my_list[j+1][placement[-1]+1] > my_list[j+1][placement[-1]+2]:
                    nx_great2 = my_list[j+1][placement[-1]+1]
                elif my_list[j+1][placement[-1]+1] < my_list[j+1][placement[-1]+2]:
                    nx_great2 = my_list[j+1][placement[-1]+2]

                # sets great to be equal to the total max sum path
                if my_list[j][placement[-1]] + nx_great > my_list[j][placement[-1]+1] + nx_great2:
                    great = my_list[j][placement[-1]]
                elif my_list[j][placement[-1]] + nx_great < my_list[j][placement[-1]+1] + nx_great2:
                    great = my_list[j][placement[-1]+1]
            else:
                # covers the last row to set great equal to the max sum path
                if my_list[j][placement[-1]] > my_list[j][placement[-1]+1]:
                    great = my_list[j][placement[-1]]
                elif my_list[j][placement[-1]] < my_list[j][placement[-1]+1]:
                    great = my_list[j][placement[-1]+1]
        else:
            great = my_list[j][0]

        if my_list[j][k] == great:
            repeat += 1

    greats.append(great)

    if repeat == 1:

        placement.append(my_list[j].index(great))

    else:
        placement.append((my_list[j].index(great, placement[-1]-1)))

print(len(greats))
print(sum(greats))
