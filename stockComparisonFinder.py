filename1 = "SPList1996 copy.txt"
filename2 = "SPList1997 copy.txt"

File1 = open(filename1,"r")
File2 = open(filename2,"r")
Dict1 = File1.readlines()
Dict2 = File2.readlines()

year1 = filename1[6:10]
year2 = filename2[6:10]

for line in Dict1:
    if Dict2.count(line) < 1:
        Dict1.remove(line)
        print(line)

with open(year1 + "-" + year2 + 'commonStocks.txt', 'w') as nf:
	for stock in Dict1:
		nf.write(stock)