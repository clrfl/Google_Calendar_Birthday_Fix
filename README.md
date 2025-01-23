# Google Calendar Birthday Fix
Google removed the possibility to show contacts birthdays within Google calendar in Germany due to legal reasons.
This script will create an importable calendar .ics file to recreate the birthday view manually.
![german removal notice](/media/removed.png)


## How to
- Navigate to https://contacts.google.com/
- Select the checkbox next to any contact
- Navigate ⋮ > Export > Select "Contacts" > Google CSV
- Run the [script](main.py) within the folder of your contacts.csv file
- Navigate to https://calendar.google.com/
- Left Sidebar "Other calendars" > + > Create new calendar > Name & Create a new calendar for birthdays
- Left Sidebar "Other calendars" > + > Import > Select your export.ics file; Select your new calendar
- Done! The color can be customized in the left sidebar
