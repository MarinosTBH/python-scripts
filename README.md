This script is a standalone script that runs in python environment to remind you of getting breaks every 30 minutes following the Pomodoro working technique(25minutes work 5 minutes relax).


Follow these steps: 

clone repo :
- git clone [git@github.com:MarinosTBH/python-scripts.git](git@github.com:MarinosTBH/python-scripts.git).
- install tk gui(tkinter) :
- sudo apt-get install python3-tk .
- Make an executable with pyinstaller (if pyinstaller is not installed follow these steps):
- pip install pyinstaller .

**The executable will be located in dist dir called : /dist/HealthReminder_modifcation** 

Now add the executable to the startup application on ubuntu:
- Open the Startup Applications Preferences window by pressing Alt+F2 or ALT + Fn + F2 to open the "Run a Command" dialog, then type gnome-session-properties and press Enter.

- In the Startup Applications Preferences window, click on the "Add" button to add a new startup application.

- In the "Add Startup Program" dialog, provide the following information:

    Name: Enter a descriptive name for your startup application, e.g., "Health Reminder".
    Command: Enter the full path to your bash script, e.g., /path/to/health_reminder.sh.
    Comment: Optionally, you can provide a brief description of your startup application.

Click on the "Add" or "Add Program" button to add your startup application.

Reboot the computer and it will be automatically compiling the script every 60 minutes to remind you.