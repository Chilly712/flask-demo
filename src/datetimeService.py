from datetime import datetime


def getTimestamp():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
