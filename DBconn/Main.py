
#! ############################################Importiere Module und Funktionen########################################################

import tkinter as tk
import csv
import mysql.connector
import schedule
import time
import ctypes
import winreg
import configparser
import os
from tkinter import Tk, ttk, Button, Entry, Label, Toplevel
from tkinter.filedialog import asksaveasfilename
from datetime import datetime, timedelta

from DBConfig import Read_Config


#! ###########################################Aufruf Unterfunktionen Def###############################################################


#! ########################################### GUI Aufruf und Hauptschleife###############################################################
# Öffne Homescreen
Main_GUI = tk.Tk()

Read_Config()

transfer_var = Read_Config()
host =transfer_var('t_host')
user =transfer_var('t_user')
database =transfer_var('t_database')

print(host)


# Starte die Hauptschleife des Fensters
Main_GUI.mainloop()
##########################################################################Fenster Config ende####################################################
