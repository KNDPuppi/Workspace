import tkinter as tk
from turtle import mainloop
from homescreen_config import configure_home_screen


GUI =tk.Tk()
configure_home_screen(GUI)
GUI = mainloop()