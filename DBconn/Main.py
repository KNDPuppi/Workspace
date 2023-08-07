
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
from tkinter import Tk, ttk, Button, Entry, Label
from tkinter.filedialog import asksaveasfilename
from datetime import datetime, timedelta


 #! ###########################################Aufruf Unterfunktionen Def###############################################################

#? def- Aufruf aller Widgets und Design Funktionen 
def HomeScreenConfig():

    Read_Config()

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

    #Button Save aktuellen Tag 
    button_DB_save_cd = tk.Button(fenster, text="SaveDay!" , command=lambda: button_DBSaveCurDay(entry))
    button_DB_save_cd .pack()

    #Button schreibe Config
    button_DB_wr_config = tk.Button(fenster, text="Save Config!" , command=lambda: Write_Config(host,user,database) )
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
    entry_host.insert(0, host)
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
   
#? def- Schreibe alle Daten aus Datenbank in ein Excelfile (mit asksaveasfilename)  
def button_DBSaveAll():
    db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database="ford1419_st2_eol"
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
  
def Write_Config(host, user, database):
         
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

    # Konfigurationsdaten in die Datei schreiben
    with open(config_file_path, 'w') as config_file:
        config.write(config_file)
#! ########################################### GUI Aufruf und Hauptschleife###############################################################
# Öffne Homescreen
fenster = tk.Tk()
#In jedem Zyklus wird die Config für das Hauptbild aufgerufen
HomeScreenConfig()










# Starte die Hauptschleife des Fensters
fenster.mainloop()
##########################################################################Fenster Config ende####################################################
