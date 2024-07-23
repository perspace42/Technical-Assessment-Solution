'''
Author: Scott Field
Version: 1.0
Purpose:
create an object to store the following attributes that will be pulled from a directory of log files:
    - pageId (string)
    - timestamp (datetime)
    - customerId (string)
'''
from datetime import datetime

class PageVisit:
    def __init__(self, customerId, pageId, timestamp):
        self.customerId = customerId
        self.pageId = pageId
        self.timestamp = timestamp

    def __str__(self):
        return f"customerId: {self.customerId}, pageId: {self.pageId}, timestamp: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
    
if __name__ == "__main__":
    print("please run the main.py file instead")