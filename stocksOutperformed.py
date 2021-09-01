startYear = 1998
endYear = 2003
timeInterval = 5

from stockComparisonFinder import FindContinuousStocks

FindContinuousStocks(startYear, endYear, timeInterval)

SPfile = open(str(startYear)+"-"+str(endYear)+".txt", 'r')
dict = SPfile.readlines()
for line in dict:
    found = False
    startOfYear = str(startYear)+"-01"
    stockFile = open(line+".us.txt", 'r')
    dict2 = stockFile.readlines()
        if not found:
            if startOfYear 
