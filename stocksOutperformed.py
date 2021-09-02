import csv
from stockComparisonFinder import FindContinuousStocks

def FindStocksThatOutperformed(start, end, interval):

    FindContinuousStocks(start, end, interval)

    SPfile = open(str(start)+"-"+str(end)+"commonStocks.txt", 'r')
    dict = SPfile.readlines()
    outperformers = []
    for line in dict:
        foundStart = False
        foundEnd = False
        startingPrice = 0
        endingPrice = 0
        startOfYear = str(start)+"-01"
        endOfYear = str(end)+"-01"
        with open(line.rstrip().lower()+".csv", 'r') as fr:
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

    return list(outperformers)