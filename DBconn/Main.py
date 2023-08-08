
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

from DBConfig import Read_Config, Write_Config
from GUIConfig import HomeScreenConfig

#! ###########################################Aufruf Unterfunktionen Def###############################################################


#! ########################################### GUI Aufruf und Hauptschleife###############################################################

def Button_write_db_config(host, user, database): 
    Write_Config(host, user,database)


# Öffne Homescreen
Main_GUI = tk.Tk()

VarTransIn_Read_Config = Read_Config()
host = VarTransIn_Read_Config['t_host']
user = VarTransIn_Read_Config['t_user']
database = VarTransIn_Read_Config['t_database']


HomeScreenConfig(Main_GUI, host, user, database, Button_write_db_config )




# Starte die Hauptschleife des Fensters
Main_GUI.mainloop()
##########################################################################Fenster Config ende####################################################
