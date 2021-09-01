import shutil
import os

filenameEnding = ".us.txt"

original = "/Users/jacknewman/Documents/GitHub/ML_Stock_Picker"
new = "/Users/jacknewman/Documents/GitHub/ML_Stock_Picker/SPHistoricalStockPrice/"

with open('/Users/jacknewman/Documents/GitHub/ML_Stock_Picker/SP500List.txt') as file:
	for line in file:
		path = line.rstrip().lower() + filenameEnding
		if os.path.exists(original+path):
			shutil.move(original+path, new+path)

