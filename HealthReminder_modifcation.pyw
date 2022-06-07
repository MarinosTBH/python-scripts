import winsound
import time
from tkinter import *
from tkinter import ttk


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
        #Label
        self.label = ttk.Label(self, text="Relax your eyes by look far(2,5meters Minimum)", font=("Arial", 18))

        self.label.pack()
        self.label = ttk.Label(self, text="Move around for 120 seconds!", font=("Arial", 18))
        self.label.pack()
        self.label = ttk.Label(self, text="Drink a cup of water to stay hydrated!", font=("Arial", 18))
        self.label.pack()
        #Button
        self.button = ttk.Button(self, text='Got it!')
        self.button['command'] = self.button_clicked
        self.button.pack()


    def button_clicked(self):
        HealthReminder.destroy(self) #works with self
beep_time = 60*30
def beep_every60():

    while True:
        winsound.Beep(1000,500)
        HealthReminder().mainloop()
        time.sleep(beep_time)

beep_every60()
