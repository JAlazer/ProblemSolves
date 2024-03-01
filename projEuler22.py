# Name Score
names = open('/Users/johan/textFiler/p022_names.txt')
assortment = names.read()

# contains all names
my_list = []

# contains a name
ls_sub = []

quotes = 0
commas = 0

# sorting the names
for i in assortment:
    ls_sub.append(i)

    # removes commas
    if i == '"':
        quotes += 1
        if quotes > 0:
            ls_sub.remove('"')
            if quotes % 2 == 0:
                my_list.append(ls_sub)
                ls_sub = []

    # removes quotes
    if i == ',':
        commas += 1
        if commas > 0:
            ls_sub.remove(',')

my_list.sort()

# alphabetical value
alpha = {'A': 1,
         'B': 2,
         'C': 3,
         'D': 4,
         'E': 5,
         'F': 6,
         'G': 7,
         'H': 8,
         'I': 9,
         'J': 10,
         'K': 11,
         'L': 12,
         'M': 13,
         'N': 14,
         'O': 15,
         'P': 16,
         'Q': 17,
         'R': 18,
         'S': 19,
         'T': 20,
         'U': 21,
         'V': 22,
         'W': 23,
         'X': 24,
         'Y': 25,
         'Z': 26}


# hold all name scores
name_scores = []

# Getting the index of each name
for j in range(len(my_list)):

    letter_sum = 0

    # going through each name
    for k in my_list[j]:

        letter_sum = letter_sum + alpha[k]

    if j == 0:
        name_scores.append(letter_sum)
    elif j > 0:
        name_scores.append(letter_sum * (j+1))

score_sum = 0

# get sum of name scores
for m in name_scores:
    score_sum = score_sum + m

print(score_sum)

