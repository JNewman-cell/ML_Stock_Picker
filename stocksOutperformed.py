import csv

def FindStocksThatOutperformed(start, end, interval):
    startYear = start
    endYear = end
    timeInterval = interval

    from stockComparisonFinder import FindContinuousStocks

    FindContinuousStocks(startYear, endYear, timeInterval)

    SPfile = open(str(startYear)+"-"+str(endYear)+".txt", 'r')
    dict = SPfile.readlines()
    outperformers = []
    for line in dict:
        foundStart = False
        foundEnd = False
        startingPrice = 0
        endingPrice = 0
        startOfYear = str(startYear)+"-01"
        endOfYear = str(endYear)+"-01"
        with open(line.lower()+".csv", 'r') as fr:
            reader = csv.reader(fr)
            for row in reader:
                if not foundStart:
                    if startOfYear in row[0]:
                        startingPrice = float(row[2])
                        foundStart = True
            for row in reader:
                if not foundEnd:
                    if endOfYear in row[0]:
                        endingPrice = float(row[2])
                        foundEnd = True
        if endingPrice/startingPrice > 1.1:
            outperformers.append(line)

    with open('SPOutperformers' + startYear + '-' + endYear + '.txt', 'w') as nf:
            for stock in outperformers:
                nf.write(stock + '\n')