import datetime

year = 1998

def get_day(year):
    d = datetime.datetime(year, 6, 1)
    offset = 1-d.weekday() #weekday = 1 means tuesday
    if offset < 0:
        offset+=7
    return d+datetime.timedelta(offset)