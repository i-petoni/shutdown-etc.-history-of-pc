# shutdown-etc.-history-of-pc
It is a an application that can be used to check the shutdown,restart,login and logoff history of a pc.

## Installing process
Its pretty easy just download the "SekureSetup.exe" file. It is a setup file which will install main application and all the necessary files this application needs to run properly.
I dont have a license or anything for this app so if for some reason your antivirus blocks it then idk do whatever you want. Turn off your antivirus if you trust me or whatever.
But i promise its not a virus or anyhting even tho its name is kinda sus but seriously i just choose this name for fun lol.

## Functions of this app
This app has three main functions
1.recent history
2.todays history
3.custom date history

You can check any (shutdown,restart,login or logoff) history.

### Disclaimer
-This app asks for admin privileges bcz it runs admin powershell scripts to get the history.
-This app can only show the history upto a specific time period. For instance restart and shutdown history of your computer can only be shown upto 4 months(1-2 days more or less) so any history older than that cannot be shwon. And logoff time period is just 7 days.
-Its because windows only stores restart and shutdown history upto 4 months and logoff for only 7 days.
-And also if you havent restated or shutdown your pc for the last 15 days it will also dont show the recent history.
-And also if you press any button that shows the history a powershell window will popup for 1-2 seconds and then close. Its bcz this app basically runs some powershell scripts to get the history so dont worry.

## About
-This program is written in python.
-Its Gui is written in tkinter.
-And its scripts are simply powershell scripts that are used to get the history of events in powershell
what these scripts basically all about is that windows stores all the events in your computer soo these scripts just req the info about specific events in this case restart,shutdown,logoff and login
using two commands "GetEventLog" and "wevtutil" both are by microsoft. Both basically gets the info about a specific event from your pc using powershell.

And that basically it.
If you wanna download the source code you can its in the rep.
Bye have a great day.🙂
