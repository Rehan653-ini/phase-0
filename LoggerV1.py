# ---Logger Version 1.0

#imports
import datetime

#Possible points according to day 

def possiblepoints():
    day = datetime.datetime.now().weekday()
    if day == 1 or day == 3:
        possible_points = 7
    if day == 6:
        possible_points = 6
    else:
        possible_points = 8
    return possible_points

#Daily Goals
def entry():
    wakeupmsg = input("Woke up by 06:00 & sent message? [Y/N]: ")
    phonedowntime = input("Phone in downtime from 16:00 to 20:45 & 21:45? [Y/N]: ")
    move = input("Walk/Exercise/Cycle/Sport done? [Y/N]: ")
    guitar = input("Practiced guitar? [Y/N]: ")
    leisuretime = input("Leisure time =< 60 mins? [Y/N]: ")
    commit = input("Build commit done? [Y/N]: ")
    Problems = input("Problems solved? [Enter number of problems]: ")
    Logtime = input("Log updated and sent by 20:45? [Y/N]: ")

#Points Achieved (Daily)
def dayscore():
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