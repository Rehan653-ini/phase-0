# ---Logger Version 1.0

#imports
import datetime
import csv

#Daily Goals
def entry():
    global wakeupmsg
    global phonedowntime
    global move
    global guitar
    global leisuretime
    global commit
    global Problems
    global Logtime

    wakeupmsg = input("Woke up by 06:00 & sent message? [Y/N]: ")
    phonedowntime = input("Phone in downtime from 16:00 to 20:45 & 21:45? [Y/N]: ")
    move = input("Walk/Exercise/Cycle/Sport done? [Y/N]: ")
    guitar = input("Practiced guitar? [Y/N]: ")
    leisuretime = input("Leisure time =< 60 mins? [Y/N]: ")
    commit = input("Build commit done? [Y/N]: ")
    Problems = input("Problems solved? [Enter number of problems]: ")
    Logtime = input("Log updated and sent by 20:45? [Y/N]: ")


#Possible points according to day 

def possiblepoints():
    global possible_points
    possible_points = 0

    day = datetime.datetime.now().weekday()
    if day == 1 or day == 3:
        possible_points = 7
    if day == 6:
        possible_points = 6
    else:
        possible_points = 8
    return possible_points

#Points Achieved (Daily)
def obtainedpoints():
    global points
    points = 0
    
    if wakeupmsg.lower() == 'y':
        points += 1
    if phonedowntime.lower() == 'y':
        points += 1
    if move.lower() == 'y':
        points += 1
    if guitar.lower() == 'y':
        points += 1
    if leisuretime.lower() == 'y':
        points += 1
    if commit.lower() == 'y':
        points += 1
    if int(Problems) >= 25:
        points += 1
    if Logtime.lower() == 'y':
        points += 1
    return points

#Day's score in percentage

def dayscore():
    global score
    score = (points / possible_points) * 100
    return score

#Call functions   
entry()
possiblepoints()
obtainedpoints()
dayscore()


#Store data to a CSV file

def updatecsv():
    f = open('LoggerV1.csv', 'a')
    #header = ['Day', 'Date', 'Possible Points', 'Points Obtained', 'Day %', 'Day Color']
    dayno = datetime.datetime.now().weekday()
    day = ''
    if dayno == 0:
        day = "Monday"
    elif dayno == 1:
        day = "Tuesday"
    elif dayno == 2:
        day = "Wednesday"
    elif dayno == 3:
        day = "Thursday"
    elif dayno == 4:
        day = "Friday"
    elif dayno == 5:
        day = "Saturday"
    else:
        day = "Sunday"
    daycolor = ''
    if score >= 85:
        daycolor = 'green'
    elif score >= 70:
        daycolor = 'amber'
    else:
        daycolor = 'red'
    date = datetime.date.today()
    record = [day, date, possible_points, points, score, daycolor]
    writer = csv.writer(f)
    writer.writerow(record)
    f.close()

#Output generation
daycolor = ''
if score >= 85:
    daycolor = 'green'
elif score >= 70:
    daycolor = 'amber'
else:
    daycolor = 'red'
print(f"Possible points: {possible_points}")
print(f"Points obtained: {points}")
print(f"Today's score: {score}% ({daycolor} day)")
update = input("Update log? [Y/N]: ")
if update.lower() == 'y':
    updatecsv()
else:
    pass