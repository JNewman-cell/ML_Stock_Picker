def FindContinuousStocks(startingYear, endingYear, timeIntervalInYears): 

    while (startingYear + timeIntervalInYears) <= endingYear:
        filename1 = "SPStocks(1996-2019)/SPList" + str(startingYear) + ".txt"
        oneInterval = startingYear+timeIntervalInYears
        filename2 = "SPStocks(1996-2019)/SPList" + str(oneInterval) + ".txt"

        File1 = open(filename1,"r")
        File2 = open(filename2,"r")
        Dict1 = File1.readlines()
        Dict2 = File2.readlines()

        for line in Dict1:
            if Dict2.count(line) < 1:
                Dict1.remove(line)

        with open(str(startingYear) + "-" + str(oneInterval) + 'commonStocks.txt', 'w') as nf:
            for stock in Dict1:
                nf.write(stock)

        startingYear+=timeIntervalInYears