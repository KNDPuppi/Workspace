
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

#? def- Aufruf aller Widgets und Design Funktionen 
def HomeScreenConfig():
    global host, user, database
    global entry_host, entry_root, entry_db, entry_pw
    
   

    style = ttk.Style(fenster)

    # Ermittle das aktuelle Fensterdesign von Windows
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
    theme = winreg.QueryValueEx(key, "AppsUseLightTheme")[0]

    # Passe das Thema an das Betriebssystem an
    if theme == 0:
        style.theme_use(themename="clam")
    else:
        style.theme_use(themename="dark")

    fenster.title("DB Collector")
    fenster.geometry("800x400")
    
    # Textfeld
    label = tk.Label(fenster, text='01') 
    label.pack(side="bottom"  )

   
    #Button Save alles
    button_DB_save_all = tk.Button(fenster, text="SaveAll!" , command=button_DBSaveAll)
    button_DB_save_all .pack()

    #Button DataBase
    button_Database = tk.Button(fenster, text="Database!" , command=open_database_settings)
    button_Database .pack()

    #Button Save aktuellen Tag 
    button_DB_save_cd = tk.Button(fenster, text="SaveDay!" , command=lambda: button_DBSaveCurDay(entry))
    button_DB_save_cd .pack()

    #Button schreibe Config
    button_DB_wr_config = tk.Button(fenster, text="Save Config!" , command=Write_Config)
    button_DB_wr_config .pack()
    
        
    # Eingabefeld für das Datum hinzufügen
    entry_label = Label(fenster, text="Datum (YYYY-MM-DD): ")
    entry_label.pack()
    entry = Entry(fenster)
    entry.pack()

     # Eingabefeld für das host
    entry_host = Label(fenster, text="Host ")
    entry_host.pack()
    entry_host = Entry(fenster)
    entry_host.pack()

      # Eingabefeld für root
    entry_root = Label(fenster, text="root ")
    entry_root.pack()
    entry_root = Entry(fenster)
    entry_root.pack()

      # Eingabefeld für Database
    entry_db = Label(fenster, text="database ")
    entry_db.pack()
    entry_db = Entry(fenster)
    entry_db.pack()

          # Eingabefeld für root
    entry_pw = Label(fenster, text="Password ")
    entry_pw.pack()
    entry_pw = Entry(fenster)
    entry_pw.pack()

    Read_Config()

    entry_host.insert(0, host)  # Führe die Einfügung erst nach dem Lesen der Konfigurationswerte durch
    entry_root.insert(0, user)
    entry_db.insert(0, database)

    
#? def- Schreibe alle Daten aus Datenbank in ein Excelfile (mit asksaveasfilename)  
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

#? def- Schreibe alle Daten eines Tages in ein Excelfile (mit asksaveasfilename)
def button_DBSaveCurDay(inputDay):
    
    db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database="ford1419_st2_eol"
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


#? Lese aktuelle Datenbank daten
def Read_Config():
    global host, user, database
    
    
    # Bestimme den Pfad zum Verzeichnis der Python-Datei
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Konstruiere den Pfad zur config.ini-Datei
    config_file_path = os.path.join(script_directory, 'config.ini')

    # Konfigurationsdatei erstellen oder laden
    config = configparser.ConfigParser()
    config.read(config_file_path)
    # Informationen aus der Konfigurationsdatei lesen
    host = config.get('Database', 'Host')
    user = config.get('Database', 'User')
    database = config.get('Database', 'Database')
  
def Write_Config():
    global host, user, database 
    global entry_host, entry_root, entry_db, entry_pw 
    
    host = entry_host.get()
    user = entry_root.get()
    database = entry_db.get()   
          
    # Bestimme den Pfad zum Verzeichnis der Python-Datei
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Konstruiere den Pfad zur config.ini-Datei
    config_file_path = os.path.join(script_directory, 'config.ini')

    # Konfigurationsdatei erstellen oder laden
    config = configparser.ConfigParser()
    config.read(config_file_path)

    # Aktualisiere die Konfigurationsdaten
    config['Database'] = {
        'Host': host,
        'User': user,
        'Database': database
    }
    print(host)
    print("Config data before writing:", config['Database'])  # Testausgabe

    # Konfigurationsdaten in die Datei schreiben
    with open(config_file_path, 'w') as config_file:
        config.write(config_file)
    print("Config data after writing:", config['Database'])  # Testausgabe


def open_database_settings():
    db_settings_window = Toplevel(fenster)
    db_settings_window.title("Database Settings")
            
#! ########################################### GUI Aufruf und Hauptschleife###############################################################
# Öffne Homescreen
fenster = tk.Tk()
#In jedem Zyklus wird die Config für das Hauptbild aufgerufen
HomeScreenConfig()




# Starte die Hauptschleife des Fensters
fenster.mainloop()
##########################################################################Fenster Config ende####################################################
