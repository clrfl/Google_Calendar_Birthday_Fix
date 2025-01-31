# Google Calendar Birthday Fix
Google has removed the ability to view contacts' birthdays within Google Calendar in Germany due to legal reasons.
This script will create an importable calendar ".ics" file to manually recreate the birthday view.
![german feature removal notice](/media/removed.png)


## How to
- Navigate to https://contacts.google.com/
- Select the checkbox next to any contact
- Navigate **⋮ > Export > Select "Contacts" > Google CSV**
- Run the [script](main.py) within the folder of your contacts.csv file to create "export.ics" (if you use [uv](https://docs.astral.sh/uv/) just call `uv run main.py`)
- Navigate to https://calendar.google.com/
- Left Sidebar **"Other calendars" > + > Create new calendar >** Name & Create a new calendar for birthdays
- Left Sidebar **"Other calendars" > + > Import >** Select your export.ics file; Select your new calendar
- **Done!** The color can be customized in the left sidebar

> [!CAUTION]
Future additions to your contacts won't sync automatically.<br>
You can either add them to your birthday calendar manually, or delete the newly created calendar every once in a while, and repeat this process.
