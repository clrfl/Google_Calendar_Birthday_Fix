# /// script
# dependencies = [
#   "pandas",
# ]
# ///

import pandas as pd

def create_entry(name, mon, day):
    return ('BEGIN:VEVENT\nSUMMARY:' + name + ' - Birthday\nDTSTART;VALUE=DATE:2025' + mon + day +
            '\nDTEND;VALUE=DATE:2025' + mon + day + '\nRRULE:FREQ=YEARLY\nTRANSP:TRANSPARENT\nEND:VEVENT\n')

with open("export.ics", "a") as f:
    f.write("BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\n")

    df = pd.read_csv('contacts.csv', delimiter=',', header=0)

    for idx, row in df.iterrows():
        if not pd.isnull(row['Birthday']):
            names = []
            if not pd.isnull(row['First Name']): names.append(row['First Name'])
            if not pd.isnull(row['Middle Name']): names.append(row['Middle Name'])
            if not pd.isnull(row['Last Name']): names.append(row['Last Name'])
            joined_name = ' '.join(names).strip()
            f.write(create_entry(joined_name, row['Birthday'].strip().split('-')[-2], row['Birthday'].strip().split('-')[-1]))

    f.write("END:VCALENDAR")
