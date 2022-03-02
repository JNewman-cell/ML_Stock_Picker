import csv
import os
import pandas as pd
from stockContinuityFinder import FindContinuousStocks

# finds all the stocks that within the S&P500 that outperformed the index within the given timeframe and interval


def FindStocksThatOutperformed(start, end, interval):
    # creating string value of start and end date to read the price data
    startOfYear = str(start)+"-01"
    endOfYear = str(end)+"-01"
    # create required files to find continuous companies
    FindContinuousStocks(start, end, interval)

    SPBenchmarkPerformance = 0.0
    if os.path.exists("../aggregateData/SP500Data.csv"):
        with open("../aggregateData/SP500Data.csv", 'r') as fr:
            # creating variables to determine if the start and end prices have been found
            foundStart = False
            foundEnd = False
            # creating variable to store start and end prices for the interval
            startingPrice = 0.0
            endingPrice = 0.0
            # create csv reader
            reader = csv.reader(fr)
            for row in reader:
                # if the starting price hasn't been found
                if not foundStart:
                    # if the starting date is true, store the price value in the variable
                    if startOfYear in row[0]:
                        startingPrice = float(row[1])
                        foundStart = True
                if foundStart:
                    # if the ending price hasn't been found
                    if not foundEnd:
                        # if the ending date is found, store the ending price value in the variable
                        if endOfYear in row[0]:
                            endingPrice = float(row[1])
                            foundEnd = True
            SPBenchmarkPerformance = endingPrice/startingPrice

    # open file of continuous companies
    SPStockfile = open(str(start)+"-"+str(end) +
                       "commonSP500Stocks.txt", 'r')
    dict = SPStockfile.readlines()
    # create list for outperforming stocks
    outperformers = {}
    for line in dict:
        # creating variables to determine if the start and end prices have been found
        foundStart = False
        foundEnd = False
        # creating variable to store start and end prices for the interval
        startingPrice = 0.0
        endingPrice = 0.0
        # check if file exists
        if os.path.exists("SP500HistoricalStockPrice/"+line.rstrip().lower()+".us.csv"):
            with open("SP500HistoricalStockPrice/"+line.rstrip().lower()+".us.csv", 'r') as fr:
                # create csv reader
                reader = csv.reader(fr)
                for row in reader:
                    # if the starting price hasn't been found
                    if not foundStart:
                        # if the starting date is true, store the price value in the variable
                        if startOfYear in row[0]:
                            startingPrice = float(row[4])
                            foundStart = True
                    if foundStart:
                        # if the ending price hasn't been found
                        if not foundEnd:
                            # if the ending date is found, store the ending price value in the variable
                            if endOfYear in row[0]:
                                endingPrice = float(row[4])
                                foundEnd = True
            # if starting price isn't found, do not add to outperformers list
            if startingPrice != 0:
                if endingPrice/startingPrice > SPBenchmarkPerformance:
                    outperformers[line] = str(endingPrice/startingPrice)
    with open(startOfYear+'-'+endOfYear+'outperformers.csv', 'w', newline='') as nf:
        fieldnames = ['Stock Ticker', 'Percent Outperformance']
        writer = csv.DictWriter(nf, fieldnames=fieldnames)

        writer.writeheader()
        for key in outperformers:
            writer.writerow(
                {'Stock Ticker': key, 'Percent Outperformance': outperformers[key]})
