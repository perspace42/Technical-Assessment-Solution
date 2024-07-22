# Technical Assessment

## Description
This is a Python Console Application that will generate a list of loyal customers as a txt file from a set of log files containing the pages
viewed by customers on a website. The log file contains the following 3 fields:
* pageId
* timestamp
* customerId

a customer is viewed as loyal if they meet the following 2 criteria:
* they visited the site each day across two days
* they visited at least two unique pages

## How To Install (Dependencies)
1: Install Python 3.12.3 from: https://www.python.org/downloads/
   be sure to add Python to your systems PATH variable during the installation

2: Clone this repository into the folder of your choice.

## How to Run
1: Either open the repository folder in an Integrated Developer Environment or Navigate to it Using The Command Prompt

2: Change directory to the project folder which should be named Technical Assessment Solution (Either in your IDE terminal or using the Command Prompt)

3: Execute this command: python main.py

## How to Test Different Log Files
Under line 38 in generateLog.py the file may be edited to alter the log files being tested
* The setupLog(name,path) function can create a new log file (returns a logger object)
* The addRecord(logger,customerId,pageId,timestamp) function can add lines to the log file

Execute this command to push any changes made to the log files: python generateLog.py

If you edit the directory you are storing the log files in, be sure the logdirectory variable on line 21 of main.py is edited to match in order to ensure the files are read by the program.



