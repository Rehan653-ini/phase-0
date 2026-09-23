
import datetime
import csv
from doctest import master
from logging import root
import tkinter as tk


def UserInterface():
    
    root = tk.Tk()
    root.title("Logger V1.0")
    root.geometry("600x400")

    entry_wokeup = tk.Entry(root)
    entry_phonedowntime = tk.Entry(root)
    entry_move = tk.Entry(root)
    entry_guitar = tk.Entry(root)
    entry_leisuretime = tk.Entry(root)
    entry_commit = tk.Entry(root)
    entry_problems = tk.Entry(root)
    entry_logtime = tk.Entry(root)
    

    entry_wokeup.grid(row=0, column=1)
    entry_phonedowntime.grid(row=1, column=1)
    entry_move.grid(row=2, column=1)
    entry_guitar.grid(row=3, column=1)
    entry_leisuretime.grid(row=4, column=1)
    entry_commit.grid(row=5, column=1)
    entry_problems.grid(row=6, column=1)
    entry_logtime.grid(row=7, column=1)
    

    tk.Label(root, text="Woke up by 06:00 & sent message? [Y/N]: ").grid(row=0, column=0)
    tk.Label(root, text="Phone in downtime from 16:00 to 20:45 & 21:45? [Y/N]: ").grid(row=1, column=0)
    tk.Label(root, text="Walk/Exercise/Cycle/Sport done? [Y/N]: ").grid(row=2, column=0)
    tk.Label(root, text="Practiced guitar? [Y/N]: ").grid(row=3, column=0)
    tk.Label(root, text="Leisure time =< 60 mins? [Y/N]: ").grid(row=4, column=0)
    tk.Label(root, text="Build commit done? [Y/N]:").grid(row=5, column=0)
    tk.Label(root, text="Problems solved? [Enter number of problems]: ").grid(row=6, column=0)
    tk.Label(root, text="Log updated and sent by 20:45? [Y/N]: ").grid(row=7, column=0)

    def submit():
        global wakeupmsg, phonedowntime, move, guitar, leisuretime, commit, problems, logtime
        wakeupmsg = entry_wokeup.get()
        phonedowntime = entry_phonedowntime.get()
        move = entry_move.get()
        guitar = entry_guitar.get()
        leisuretime = entry_leisuretime.get()
        commit = entry_commit.get()
        problems = entry_problems.get()
        logtime = entry_logtime.get()

        
        print(f"Woke up: {wakeupmsg}")
        print(f"Phone downtime: {phonedowntime}")
        print(f"Move: {move}")
        print(f"Guitar: {guitar}")
        print(f"Leisure time: {leisuretime}")
        print(f"Commit: {commit}")
        print(f"Problems: {problems}")
        print(f"Log time: {logtime}")

        return all

    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.grid(row=8, column=0, columnspan=2)



    root.mainloop()

UserInterface()

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
    if int(problems) >= 25:
        points += 1
    if logtime.lower() == 'y':
        points += 1
    return points

#Day's score in percentage

def dayscore():
    global score
    score = (points / possible_points) * 100
    return score

#Call functions   
possiblepoints()
obtainedpoints()
dayscore()

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