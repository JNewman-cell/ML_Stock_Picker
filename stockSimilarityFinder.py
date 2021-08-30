import csv

i = 1996
while i < 2020:
    year = str(i)
    #Q2changes = year + "-04"
    #Q3changes = year + "-07"
    #Q4changes = year + "-10"

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

    #Q1 Changes to the SP
    '''
    with open('SP500HistoricalComponents.csv', 'r') as fr:
        reader = csv.reader(fr)
        for row in reader:
            if not found:
                if year in row[0]:
                    temp = row[1].rsplit(',')
                    found = True
                    for ticker in temp:
                        SPList.append(ticker)

    with open('SPList' + year + 'Q1.txt', 'w') as nf:
        for stock in SPList:
            nf.write(stock + '\n')
    '''

    #Q2 Changes to the SP
    '''
    with open('SP500HistoricalComponents.csv', 'r') as fr:
        reader = csv.reader(fr)
        for row in reader:
            if not found:
                if Q2changes in row[0]:
                    temp = row[1].rsplit(',')
                    found = True
                    for ticker in temp:
                        SPList.append(ticker)

    with open('SPList' + year + 'Q2.txt', 'w') as nf:
        for stock in SPList:
            nf.write(stock + '\n')
    '''

    #Q3 Changes to the SP
    '''
    with open('SP500HistoricalComponents.csv', 'r') as fr:
        reader = csv.reader(fr)
        for row in reader:
            if not found:
                if Q3changes in row[0]:
                    temp = row[1].rsplit(',')
                    found = True
                    for ticker in temp:
                        SPList.append(ticker)

    with open('SPList' + year + 'Q3.txt', 'w') as nf:
        for stock in SPList:
            nf.write(stock + '\n')
    '''

    #Q4 Changes to the SP
    '''
    with open('SP500HistoricalComponents.csv', 'r') as fr:
        reader = csv.reader(fr)
        for row in reader:
            if not found:
                if Q4changes in row[0]:
                    temp = row[1].rsplit(',')
                    found = True
                    for ticker in temp:
                        SPList.append(ticker)

    with open('SPList' + year + 'Q4.txt', 'w') as nf:
        for stock in SPList:
            nf.write(stock + '\n')
    '''
            
    i+=1
