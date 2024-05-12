#Abdul-Kader Jainoodien
#JNDABD002
#A program to convert one format of time to another

#Takes the formatted input
inputStr=input("Enter the date and time (yyyy-mm-dd hh:mm):\n")

#Isolates and formats the year
year="'"+inputStr[2:4]

#Isolates and formats the month using a dictionary
months={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
month=months[int(inputStr[5:7])]

#Isolates and formats the day
day=int(inputStr[8:10])
if day in [1,21,31]:
    day=str(day)+"st"
elif day in [2,22]:
    day=str(day)+"nd"
elif day in [3,23]:
    day=str(day)+"rd"
else:
    day=str(day)+"th"

#Isolates and formats the time (and isolates the hours).
time=inputStr[11:]
timeSuf="am"
timeH=int(time[:2])
timeM=time[2:]
if timeH>=12: #Checks for pm and rectifies into 12 hour format.
    timeH-=12
    timeSuf="pm"
if timeH==0: #Rectifies into 12 hour format if time is 00 (from rectifying or otherwise).
    timeH=12
time=str(timeH)+timeM+" "+timeSuf

print(f"{time} on the {day} of {month} {year}")