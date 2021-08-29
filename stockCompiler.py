import csv

temp = []
EveryStockInSP = []

with open('S&P500HistoricalComponents.csv', 'r' ) as fr:
	reader = csv.reader(fr)
	for row in reader:
		temp = row[1].rsplit(",")
		for ticker in temp:
			if EveryStockInSP.count(ticker) < 1:
				EveryStockInSP.append(ticker)

EveryStockInSP.pop(0)

with open('S&PList.txt', 'w') as nf:
	for stock in EveryStockInSP:
		nf.write(stock + "\n")