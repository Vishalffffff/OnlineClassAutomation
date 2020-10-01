#This Script Can be used to attend Different Classes at different time with different URL. But In My Case I am having same URL for everyclass, everyday so I am not using Excel File with TIME SCHEDULE and Links
#You May Use a Excel File with time and Link to join classes through different URLs.
#To do so remove '#' from comments

#<!-----RKGIT MEET AUTOMATION BY VISHAL SRIVASTAVA----->

# MAKE SURE YOU ARE LOGGED IN BEFORE RUNNING THIS SCRIPT 


import pyautogui as py  #Install Pyautogui for automation .
from time import sleep
import webbrowser
#import openpyxl

#RKGIT-MEET AUTOMATION, ATTEND CLASSES AUTOMATICALLY.....

#def getMeetLink(day,hour):
  
   # path='AutomationTimeTable.xlsx'     # Enter your path of the Excelfile      
   # wb = openpyxl.load_workbook(path)
    #sheet = wb['Sheet1']
   # link = sheet.cell(row=day+1,column=hour+1).value
   # return link                                             # returns the class link from excel file
   
def attendGclass(): 
# Get co-ordinates of the different Buttons using Pyautogui ; 
     joinX,joinY = 95,879                # Enter (x,y) position of join button
     listenX,listenY = 1054,594           #Enter (x,y) position of listen Only Button
    # chatIconX,chatIconY = 266,976       # Enter (x,y) position of chatIcon button
     chatboxX,chatboxY = 266,976         # Enter (x,y) position of chatbox button
     sendX,sendY = 627,970               # Enter (x,y) position of send button
    
   #  url = str(getMeetLink(day,hour))
     url = 'https://my.rkgitlms.in/mod/bigbluebuttonbn/view.php?id=56'
     webbrowser.open_new(url)  # open  web browser
     sleep(15)
     py.click(joinX,joinY)    # click to join session
     sleep(15)
     py.click(listenX,listenY) # Use listen only 
     sleep(12)
     #py.click(chatIconX,chatIconY) 
     #sleep(3)
     py.click(chatboxX,chatboxY)  # Click on message Box 
     py.write("Yes mam",interval=0.25)     # Enters the Greeting message
     sleep(2)
     py.click(sendX,sendY)
     #sleep(1)
     #ss= py.screenshot()                          # Takes Screenshot of the screen
     #ss.save('\Class')               # Enter Location where to save the screenshot file
     sleep(100)                                  # It sleeps for 1hour


#day = int(input('Enter the day order: '))
#hour = int(input('Enter which class hour: '))
attendGclass()

#To make code simple this code have functionality to attend only one class but you can modify code for whole day by just adding sleep(3600) & calling attendGclass() again.
#Contact Me for any doubt INSTAGRAM: srivishal.27

#P.S. Python is Love.




    



