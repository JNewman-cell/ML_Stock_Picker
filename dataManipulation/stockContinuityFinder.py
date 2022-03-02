# finds stocks that were in the S&P500 in the given timeframe every year
# parameters are the start year of the desired data, the end of the desired data, and the time interval of the data
def FindContinuousStocks(startingYear, endingYear, timeIntervalInYears):
    # for every time interval within the start and end year
    while (startingYear + timeIntervalInYears) <= endingYear:
        # create the filenames for the desired years
        filename1 = "SPStocks(1996-2019)/SPList" + str(startingYear) + ".txt"
        oneInterval = startingYear+timeIntervalInYears
        filename2 = "SPStocks(1996-2019)/SPList" + str(oneInterval) + ".txt"

        # open the files of the years and read them into dictionaries
        File1 = open(filename1, "r")
        File2 = open(filename2, "r")
        Dict1 = File1.readlines()
        Dict2 = File2.readlines()

        # for every ticker dictionary 1, check if it was within dictionary 2, and remove it if it was
        for line in Dict1:
            if Dict2.count(line) < 1:
                Dict1.remove(line)

        # create a file with the stocks that were still in the S&P 500 in the start and end year
        with open(str(startingYear) + "-" + str(oneInterval) + 'commonSP500Stocks.txt', 'w') as nf:
            for stock in Dict1:
                nf.write(stock)

        startingYear += timeIntervalInYears
