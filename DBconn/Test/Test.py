import tkinter as tk
from homescreen_config import configure_home_screen


GUI =tk.Tk()
configure_home_screen(GUI)
GUI.mainloop()





#####################################################
#######################################################
#####################################################



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


 #! ###########################################Aufruf Unterfunktionen Def###############################################################

#! def- Aufruf aller Widgets und Design Funktionen 
def HomeScreenConfig(Main_GUI):
         
   
    style = ttk.Style(Main_GUI)

    # Ermittle das aktuelle Fensterdesign von Windows
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
    theme = winreg.QueryValueEx(key, "AppsUseLightTheme")[0]

    # Passe das Thema an das Betriebssystem an
    if theme == 0:
        style.theme_use(themename="clam")
    else:
        style.theme_use(themename="dark")

    Main_GUI.title("DB Collector")
    Main_GUI.geometry("800x400")
    
    # Textfeld
    label = tk.Label(Main_GUI, text='01') 
    label.pack(side="bottom"  )

   
    #Button Save alles
    button_DB_save_all = tk.Button(Main_GUI, text="SaveAll!" , command=button_DBSaveAll)
    button_DB_save_all .pack()

    #Button DataBase
    button_Database = tk.Button(Main_GUI, text="Database!" , command=open_database_settings)
    button_Database .pack()

    #Button Save aktuellen Tag 
    button_DB_save_cd = tk.Button(Main_GUI, text="SaveDay!" , command=lambda: button_DBSaveCurDay(entry))
    button_DB_save_cd .pack()

    #Button schreibe Config
    button_DB_wr_config = tk.Button(Main_GUI, text="Save Config!" , command=Write_Config)
    button_DB_wr_config .pack()
    
        
    # Eingabefeld für das Datum hinzufügen
    entry_label = Label(Main_GUI, text="Datum (YYYY-MM-DD): ")
    entry_label.pack()
    entry = Entry(Main_GUI)
    entry.pack()

     # Eingabefeld für das host
    entry_host = Label(Main_GUI, text="Host ")
    entry_host.pack()
    entry_host = Entry(Main_GUI)
    entry_host.pack()

      # Eingabefeld für root
    entry_root = Label(Main_GUI, text="root ")
    entry_root.pack()
    entry_root = Entry(Main_GUI)
    entry_root.pack()

      # Eingabefeld für Database
    entry_db = Label(Main_GUI, text="database ")
    entry_db.pack()
    entry_db = Entry(Main_GUI)
    entry_db.pack()

          # Eingabefeld für root
    entry_pw = Label(Main_GUI, text="Password ")
    entry_pw.pack()
    entry_pw = Entry(Main_GUI)
    entry_pw.pack()
  

    entry_host.insert(0, host)  # Führe die Einfügung erst nach dem Lesen der Konfigurationswerte durch
    entry_root.insert(0, user)
    entry_db.insert(0, database)

    
#! def- Schreibe alle Daten aus Datenbank in ein Excelfile (mit asksaveasfilename)  
def button_DBSaveAll():
    global host, user, database
    
    db_connection = mysql.connector.connect(
    host= host,
    user=user,
    database=database
    )
    cursor = db_connection.cursor()

    select_query = "SELECT * FROM prozessdaten"
    cursor.execute(select_query)
    results = cursor.fetchall()

    root = Tk()
    root.withdraw()

    file_path = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Dateien", "*.csv")])

     # CSV-Datei zum Schreiben öffnen
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Spaltennamen schreiben
        column_names = [i[0] for i in cursor.description]
        csv_writer.writerow(column_names)

        # Daten in CSV schreiben
        csv_writer.writerows(results)

    # Verbindung und Cursor schließen
    cursor.close()
    db_connection.close()
     # Schließe das Wurzelfenster, nachdem die Aktionen abgeschlossen sind
    root.destroy()

#! def- Schreibe alle Daten eines Tages in ein Excelfile (mit asksaveasfilename)
def button_DBSaveCurDay(inputDay):
    
    db_connection = mysql.connector.connect(
    host= host,
    user=user,
    database=database
    )
    cursor = db_connection.cursor()
    date= inputDay.get()

   
    select_query = "SELECT * FROM prozessdaten WHERE DATE(timestamp) = '" + date + "'"
    cursor.execute(select_query)
    results = cursor.fetchall()


    root = Tk()
    root.withdraw()

    file_path = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Dateien", "*.csv")])

     # CSV-Datei zum Schreiben öffnen
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Spaltennamen schreiben
        column_names = [i[0] for i in cursor.description]
        csv_writer.writerow(column_names)

        # Daten in CSV schreiben
        csv_writer.writerows(results)

   # Verbindung und Cursor schließen
    cursor.close()
    db_connection.close()
     # Schließe das Wurzelfenster, nachdem die Aktionen abgeschlossen sind
    root.destroy()





#! ########################################### Neues Fenster Toplevel ###############################################################   
def open_database_settings():
    db_settings_window = Toplevel(Main_GUI)
    db_settings_window.title("Database Settings")
            
#! ########################################### GUI Aufruf und Hauptschleife###############################################################
# Öffne Homescreen
Main_GUI = tk.Tk()

#In jedem Zyklus wird die Config für das Hauptbild aufgerufen

HomeScreenConfig()




# Starte die Hauptschleife des Fensters
Main_GUI.mainloop()
##########################################################################Fenster Config ende####################################################
