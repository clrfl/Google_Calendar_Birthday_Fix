# /// script
# dependencies = [
#   "pandas",
#   "datetime"
# ]
# ///

import pandas as pd
import datetime

# Google Calendar full days events are supposed to end on the next day 
def increment_day(mon, day):
    date = datetime.date(datetime.date.today().year, int(mon), int(day))
    next_day = date + datetime.timedelta(days=1)
    # fill for 0102 dates
    return str(next_day.month).zfill(2)+ str(next_day.day).zfill(2)

def create_entry(name, mon, day, reminder):
    entry_string = ('BEGIN:VEVENT\nSUMMARY:' + name + ' - Birthday\nDTSTART;VALUE=DATE:2025' + mon + day +
            '\nDTEND;VALUE=DATE:2025' + increment_day(mon, day) + '\nRRULE:FREQ=YEARLY\nTRANSP:TRANSPARENT')
    # Add a reminder
    if(reminder):
        entry_string += ('\nBEGIN:VALARM\nACTION:DISPLAY\nDESCRIPTION:Reminder\n'+
        # Trigger formatting: 0D -> 0 days prior, T9H0M0S -> Time 9:00:00
        'TRIGGER:P0DT9H0M0S\nEND:VALARM')
    entry_string += '\nEND:VEVENT\n'
    return entry_string
            
# Use utf-8 encoding for special characters i.e. ä, ü, ö in german
with open("export.ics", "w", encoding='utf-8') as f:
    f.write("BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\n")

    df = pd.read_csv('contacts.csv', delimiter=',', header=0)

    for idx, row in df.iterrows():
        if not pd.isnull(row['Birthday']):
            names = []
            if not pd.isnull(row['First Name']): names.append(row['First Name'])
            if not pd.isnull(row['Middle Name']): names.append(row['Middle Name'])
            if not pd.isnull(row['Last Name']): names.append(row['Last Name'])
            joined_name = ' '.join(names).strip()
            f.write(create_entry(joined_name, row['Birthday'].strip().split('-')[-2], row['Birthday'].strip().split('-')[-1], reminder=True))
            
    f.write("END:VCALENDAR")
