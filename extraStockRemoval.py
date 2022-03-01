# removes extra files of stock prices that are not in our dataset
import shutil
import os

# original filename ending
filenameEnding = ".us.txt"

original = "oldPathname"
new = "newPathname"


with open('oldPathname/SP500List.txt') as file:
    # for every historical stock in the S&P500
    for line in file:
        # put line in lower case and add filename
        path = line.rstrip().lower() + filenameEnding
        # if the file exists, move it to the new file
        if os.path.exists(original+path):
            shutil.move(original+path, new+path)
