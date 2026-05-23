#Logs study sessions with subject, duration, and date, then shows statistics
#Log session (datetime library), calculate totals, find busiest subject, display report
'''
Owen Powell
IS 303 - A04

Study Timer
This program lets you log your study sessions by subject. 

Inputs:
- which subject you are studying


Processes:
- get_valid_string() - I: subject name by the user P:make sure it isn't left blank or only spaces 
O: return the variable subject

- start_logging() I: get the subject name using get_valid_string() P: start the time tracking O: return the 
start_timestamp, date, and subject variables

- end_logging(subject, start_timestamp) I: takes in subject and start_timestamp P: ends time tracking, 
creates end_timestamp variable. Then does end_timestamp - start_timestamp to get the total time for each session.
O: adds subject and time, and date to a list of dictionaries (called sessions = []) to track
 individual sessions. 

- calculate_totals(sessions) I: takes in the sessions list P: loops through list, adding up session totals
 O: puts this info in a new dictionary. totals = {}

-find_busiest(totals) I: takes in the totals dictionary P: loops through it to find the subject with the most 
time spent studying O: returns the variable busiest_subject

display_report(sessions, busiest_subject, totals) - loop through the list of sessions and display the info in a formatted way.

Outputs:
- Report that shows the individual study sessions and how long they were, and shows the busiest subject.
Example Output:
Sessions: 
1. Statistics --- 60 min --- 5/22/2026
2. Spanish --- 30 min --- 5/22/2026
3. Information Systems --- 40 min --- 5/22/2026
4. Statistics --- 40 min --- 5/22/2026

Totals:
Statistics --- 100 min
Spanish --- 30 min
Information Systems --- 40 min

Busiest Subject: Statistics
'''
from datetime import datetime
sessions = []
def get_valid_string():
    while True:
        subject = input("What subject are you studying?").title()
        if not subject.strip():
            print("Please enter a subject name.")
        else:
            return subject

# start_logging() I: get the subject name using get_valid_string() P: start the time tracking O: return the 
# start_timestamp, date, and subject variables
def start_logging():
    subject = get_valid_string()
    start_timestamp = datetime.now()
    return start_timestamp, subject


# - end_logging(subject, start_timestamp) I: takes in subject and start_timestamp P: ends time tracking, 
# creates end_timestamp variable. Then does end_timestamp - start_timestamp to get the total time for each session.
# O: adds subject and time, and date to a list of dictionaries (called sessions = []) to track
#  individual sessions. 
def end_logging(start_timestamp, sessions, subject):
    end_timestamp = datetime.now()
    session_time = round(((end_timestamp - start_timestamp).total_seconds())/60, 2)
    sessions.append({"subject":subject, 
                     "time":session_time,
                    "date":end_timestamp.date()})

# - calculate_totals(sessions) I: takes in the sessions list P: loops through list, adding up session totals
#  O: puts this info in a new dictionary. totals = {}
def calculate_totals(sessions):
    totals = {}
    for session in sessions:
        if session["subject"] not in totals:
            totals[session["subject"]] = session["time"]
        else:  
            totals[session["subject"]] += session["time"]
    return totals
    
# -find_busiest(totals) I: takes in the totals dictionary P: loops through it to find the subject with the most 
# time spent studying O: returns the variable busiest_subject
def find_busiest(totals):
    busiest_subject = max(totals, key=lambda x: totals[x])
    return busiest_subject




def display_report(sessions, totals, busiest_subject):
    print(f"Sessions:")
    for index, session in enumerate(sessions, 1):
        print(f"{index}. {session['subject']} --- {session['time']} min --- {session['date']}")
    print(f"Totals:")
    for subject, time in totals.items():
        print (f"{subject} --- {time} min")
    print(f"Busiest Subject: {busiest_subject}")

#Main Program
intro_message = "Hello! Use this study timer tool to track your study sessions for each subject you are studying!"
track_another = "yes"
print(intro_message)
while track_another == "yes":
    start_input = input("Enter in 'start' to start logging a study session! ").lower()
    if start_input == "start":
        start_timestamp, subject = start_logging()
        stop_input = input("Enter in 'stop' when you are done with the session. ").lower()
        if stop_input == "stop":
            end_logging(start_timestamp, sessions, subject)
            track_another = input("Would you like to add another? (yes/no) ").lower()
totals = calculate_totals(sessions)
busiest_subject = find_busiest(totals)
display_report(sessions, totals, busiest_subject)
        


