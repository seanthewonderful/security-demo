
open_file = open("CupcakeInvoices.csv")

for line in open_file: 
    print(line)

for line in open_file:
    line = line.rstrip('\n').split(',')
    print(line[2])
total = 0 
newtot = timesd
total += newtot

for line in open_file:
    line = line.rstrip('\n').split(',')
    print(int(line[3])*float(line[4]))

    x = int(line[3])*float(line[4])
    print(x)

total = 0

for line in open_file:
    line = line.rstrip('\n').split(',')
    inv_tot = (int(line[3])*float(line[4]))
    total += inv_tot

    # x = int(line[3])*float(line[4])
    # y = sum(x)
    # print(y)
    # print(line)
    # line = line.rstrip('\n').split(',')
    # x = float(line[3])
    # print(x)
    # quantity = []
    # quantity.append(x)
    # print(quantity)
    # quantity.append(line[3])
    # print(quantity)
    # x = float(line[3])*float(line[4])
    # print(sum(x))
    # quans.append(line[3])
    # x = float(line[3])
    # xsum = sum(x)
    # y = float(line[4])
    # ysum = sum(y)
    # print(xsum, ysum)
    # omg how can python not sum this together in a simpler way
print(format(total,".2f"))

open_file.close()