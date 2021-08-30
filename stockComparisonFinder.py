startingYear = 1996
timeIntervalInYears = 5

while startingYear + timeIntervalInYears < 2020:
    filename1 = "SPList" + str(startingYear) + "copy.txt"
    filename2 = "SPList" + str(startingYear+timeIntervalInYears) + "copy.txt"

    File1 = open(filename1,"r")
    File2 = open(filename2,"r")
    Dict1 = File1.readlines()
    Dict2 = File2.readlines()

    for line in Dict1:
        if Dict2.count(line) < 1:
            Dict1.remove(line)
            print(line)

    with open(str(startingYear) + "-" + str(startingYear+timeIntervalInYears) + 'commonStocks.txt', 'w') as nf:
        for stock in Dict1:
            nf.write(stock)

    startingYear+=timeIntervalInYears