import datetime

def get_day(dateFormat="%Y%m%d", addDays=0):
    timeNow = datetime.datetime.now()
    if (addDays != 0):
        anotherTime = timeNow + datetime.timedelta(days=addDays)
    else:
        anotherTime = timeNow

    return anotherTime.strftime(dateFormat)