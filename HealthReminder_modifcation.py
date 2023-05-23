import os
import time
import logging
from tkinter import *
from tkinter import ttk

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Create a stream handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Add both handlers to the logger
logger = logging.getLogger('')
logger.addHandler(stream_handler)

class HealthReminder(Tk):
    def __init__(self):
        super().__init__()

        self.title_ = "Health Reminder!"
        self.title(self.title_)

        self.bg = "#263D42"
        self.fg = "#cccccc"
        self["bg"] = self.bg

        self.__width_scr__ = self.winfo_screenwidth()
        self.__height_scr__ = self.winfo_screenheight()

        self.width_perc = 0.40
        self.height_perc = 0.20

        self.__width_app__ = int(self.__width_scr__ * self.width_perc)
        self.__height_app__ = int(self.__height_scr__ * self.height_perc)

        self.central_l_window = int((self.__width_scr__ // 2) - (self.__width_app__ // 2) + 2)
        self.central_a_window = int((self.__height_scr__ * (1 - self.height_perc)) // 2)

        self.__center__ = f"{self.__width_app__}x{self.__height_app__}+{self.central_l_window}+{self.central_a_window}"

        self.geometry(self.__center__)
        # Label
        self.label = ttk.Label(self, text="Relax your eyes by looking far (2.5 meters minimum)", font=("Arial", 18))
        self.label.pack()
        self.label = ttk.Label(self, text="Move around for 120 seconds!", font=("Arial", 18))
        self.label.pack()
        self.label = ttk.Label(self, text="Drink a cup of water to stay hydrated!", font=("Arial", 18))
        self.label.pack()
        # Button
        self.button = ttk.Button(self, text='Got it!')
        self.button['command'] = self.button_clicked
        self.button.pack()

        # Start the application log
        logging.info('Application started.')

    def button_clicked(self):
        # Stop the application log
        logging.info('Application stopped.')

        HealthReminder.destroy(self)

def beep_every60():
    beep_time = 60 * 30 

    while True:
        # Play system sound
        os.system("paplay /usr/share/sounds/freedesktop/stereo/complete.oga &")

        # Create and run HealthReminder instance
        reminder = HealthReminder()
        reminder.mainloop()

        time.sleep(beep_time)

if __name__ == '__main__':
    # Start the main log
    logging.info('Script execution started.')

    # Run the application
    try:
        beep_every60()
    except Exception as e:
        logging.exception('An error occurred: %s', str(e))

    # Stop the main log
    logging.info('Script execution stopped.')
