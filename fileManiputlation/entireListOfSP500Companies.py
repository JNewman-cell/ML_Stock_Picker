# compiles an entire list of stocks that were in the S&P500 in the timeframe of our dataset
import csv

# temporary array for storing stocks
temp = []
# compiled list of every stock that has been in the S&P 500 for our dataset
EveryStockInSP = []

# go through all the historical stock components of the S&P500 and check if the ticker has been added to the main list
with open('SP500HistoricalComponents.csv', 'r') as fr:
    reader = csv.reader(fr)
    for row in reader:
        # create a list without commas of each row of the historical list of stocks file, skipping the date of the csv
        temp = row[1].rsplit(",")
        # for  every stock
        for ticker in temp:
            # checks if the ticker is already in the main list of historical tickers
            if EveryStockInSP.count(ticker) < 1:
                # if the ticker is not in the historical list of stocks, then add the ticker to the main list
                EveryStockInSP.append(ticker)

# remove the header of the csv file
EveryStockInSP.pop(0)

# create a csv with every stock that has been in the S&P 500 for our dataset
with open('test1.txt', 'w') as nf:
    for stock in EveryStockInSP:
        nf.write(stock + "\n")
