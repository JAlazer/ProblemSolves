# Number Letter counts
# not solved!!!
counter = 0
singles = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
tens_index = 0
hundred = 'hundredand'

for i in singles:
    counter += len(i)
for a in teens:
    counter += len(a)
for c in tens:
    counter += len(c)

# double digits
for e in tens:
    for f in singles:
        dub_dig = e + f
        counter += len(dub_dig)

# hundred singles
for h in singles:
    for k in singles:
        f_hundo = h + hundred + k
        counter += len(f_hundo)

# Hundred teens
for m in singles:
    for n in teens:
        hun_teen = m + hundred + n
        counter += len(hun_teen)

# Hundred tens
for p in singles:
    for q in tens:
        hun_tens = p + hundred + q
        counter += len(hun_tens)

# Hundred double tens
for s in singles:
    for t in tens:
        for u in singles:
            hun_dub_ten = s + hundred + t + u
            counter += len(hun_dub_ten)

thousand = 'one thousand'
counter += len(thousand)-1
print(counter)
# 21124





