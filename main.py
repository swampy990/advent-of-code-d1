

infile = open("cals.txt")
Lines = infile.readlines()
caltot = 0
callist = []

for line in Lines:

    if not line.strip():
        callist.append(caltot)
        caltot = 0
    else:
        caltot = caltot + int(line)

print("Top elf is " + str((sorted(callist, reverse=True)[:1])))
print("Total for top three is " + str(sum(sorted(callist, reverse=True)[:3])))



