'''
Author: Scott Field
Version: 1.0
Name: Generate Loyal Customer List
Purpose:
Generate a list of loyal customers as a txt file from a set of log files containing the pages
viewed by customers on a website. The log file contains:
    - pageId
    - timestamp
    - customerId
a customer is viewed as loyal if they meet the following criteria:
    - they visited the site each day across two days
    - they visited at least two unique pages
'''

import os
from datetime import datetime
from PageVisit import PageVisit

#set directory to find relevant log files
logDirectory = "logs/"
#initialize dictionary of pageVisits
visitDict = {}
#set format to process timestamps
dateFormat = "%Y-%m-%d %H:%M:%S"

#get the value from a string between name and end
def getValue(name, string, end = ","):
    #Find where the parameter name ends then offset it to save where the value starts
    startPos = string.index(name) + len(name) + 2
    #Find the next end after the starting position to determine where the value lies
    endPos = string.find(end, startPos)
    #Pull the value between the starting and ending position
    value = line[startPos : endPos].strip()
    return value

#Test if the currently selected PageVisit indicates that the customer is loyal
def testValues(visitList,outerIndex):
    #get the first PageVisit
    currentVisit = visitList[outerIndex]
    #test it against all subsequent PageVisits
    for innerIndex in range(outerIndex + 1,length):
        nextVisit = visitList[innerIndex]
        #Check if the PageVisits were on consecutive days
        daysPassed = (nextVisit.timestamp - currentVisit.timestamp).days
        if (daysPassed == 1):
            #Check if the PageVisits were to different pages
            if nextVisit.pageId != currentVisit.pageId:
                return True
    
    return False
                

#main loop
if __name__ == "__main__":
    for fileName in os.listdir(logDirectory):
        path = os.path.join(logDirectory,fileName)

        #Ensure that path leads to a log file
        if os.path.isfile(path) and fileName.endswith('.log'):
            #Open the file
            with open(path,'r') as file:
                for line in file:
                    try:
                        #Attempt to get the data from the log file
                        customerId = getValue(name = "customerId", string = line)
                        pageId = getValue(name = "pageId", string = line)
                        dateString = getValue(name = "timestamp", string = line, end = "\n")
                        
                        #Convert string into datetime object
                        timestamp = datetime.strptime(dateString,dateFormat)

                        #Assign the data to the class
                        visit = PageVisit(customerId,pageId,timestamp)
                       
                        #Assign the customerID to a list containing all PageVisits with that customer ID
                        visitDict.setdefault(customerId,[]).append(visit)

                    except Exception as e:
                        print(f"The error: {e} occurred while attempting to read data from the log file")
                        #end program
                        exit()

    
    #Iterate across values to generate list of loyal customers
    loyalCustomers = []
    #Get the list of PageVisits from each specific customer
    for key, visitList in visitDict.items():
        #sort PageVists by timestamp in ascending order
        visitList.sort()
        #print(key)
        length = len(visitList)
        #iterate across list to determine which customers are loyal
        for outerIndex in range(length - 1):
            #get the first PageVisit
            if testValues(visitList,outerIndex):
                #Add customer to list of loyal customers
                loyalCustomers.append(key)
                #move on to the next Customer PageVisits
                break
 
    #Generate the file that stores the list of loyal customers
    try:
        file = open("LoyalCustomers.txt",'w')

        for customer in loyalCustomers:
            file.write(f"CustomerId: {customer}\n")
    
    except Exception as e:
        print(f"The error {e} occurred while attempting to generate the list of loyal customers")