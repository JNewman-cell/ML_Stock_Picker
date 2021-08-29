import shutil
import os

filenameEnding = ".us.txt"

original = "/Users/jacknewman/Documents/GitHub/ML_Stock_Picker/stockPriceData/"
new = "/Users/jacknewman/Documents/GitHub/ML_Stock_Picker/S&PHistoricalStockPrice"

with open('S&PList.txt') as file:
	for line in file:
		path = line.rstrip().lower() + filenameEnding
		if os.path.exists(original+path):
			shutil.move(original+path, new+path)

