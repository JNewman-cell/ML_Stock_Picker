import csv

i = 1999
while i < 2020:
    year = str(i)
    SPList = []
    found = False

    with open('SP500HistoricalComponents.csv', 'r') as fr:
        reader = csv.reader(fr)
        for row in reader:
            if not found:
                if year in row[0]:
                    temp = row[1].rsplit(',')
                    found = True
                    for ticker in temp:
                        SPList.append(ticker)



    with open('SPList' + year + '.txt', 'w') as nf:
        for stock in SPList:
            nf.write(stock + '\n')
            
    i+=1
