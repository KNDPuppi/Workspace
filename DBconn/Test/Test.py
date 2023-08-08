import tkinter as tk
from turtle import mainloop
from homescreen_config import configure_home_screen


GUI =tk.TK()
configure_home_screen(GUI)
GUI = mainloop()