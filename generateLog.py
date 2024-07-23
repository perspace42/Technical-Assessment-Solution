'''
Author: Scott Field
Version: 1.0
Name: Generate Log
Purpose:
Run this file to generate the log files to be used in testing the application, log files will contain:
    - pageId
    - timestamp
    - customerId

firstLog represents the log file for 2 days ago
secondLog represents the log file for yesterday
thirdLog represents the log file for today
'''

import logging #To create the necessary log files
from datetime import datetime, timedelta

#Create a new log file
def setupLog(name, path):
    formatter = logging.Formatter('%(message)s')
    handler = logging.FileHandler(path, mode="w")        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level=logging.INFO)
    logger.addHandler(handler)

    return logger

#Create a record in a log file
def addRecord(logFile, customerId, pageId, timestamp):
    message = f"customerId: {customerId}, pageId: {pageId}, timestamp: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
    logFile.info(message)


#If this file is being run to generate the logs
if __name__ == "__main__":
    #Generate Logs
    firstLog = setupLog("log1","logs/log1.log")
    secondLog = setupLog("log2", "logs/log2.log")
    thirdLog = setupLog("log3","logs/log3.log")

    #Set Times
    today = datetime.now()
    yesterday = today - timedelta(days = 1)
    b4yesterday = yesterday - timedelta(days = 1)

    #Add Customer Access Records to Logs

    #Accessed two unique pages across same day
    addRecord(thirdLog,customerId = "123", pageId = "1", timestamp = today)
    addRecord(thirdLog,customerId = "123", pageId = "2", timestamp = today)

    #Accessed two unique pages across two non consecutive days
    addRecord(thirdLog,customerId = "456", pageId = "4", timestamp = today)
    addRecord(firstLog,customerId = "456", pageId = "4", timestamp = b4yesterday)

    #Accessed two unique pages across two consecutive days
    addRecord(secondLog,customerId = "789", pageId = "3", timestamp = yesterday)
    addRecord(secondLog,customerId = "789", pageId = "4", timestamp = today)

    #Accessed two of the same page across two consecutive days
    addRecord(thirdLog, customerId = "000", pageId = "6", timestamp = today)
    addRecord(secondLog,customerId = "000", pageId = "6", timestamp = yesterday)

    #Accessed two of the same page across two consecutive days with a non related record in between
    addRecord(firstLog,customerId = "117",pageId = "004", timestamp = today)
    addRecord(firstLog,customerId = "117",pageId = "005", timestamp = today)
    addRecord(firstLog,customerId = "117",pageId = "004", timestamp = yesterday)


