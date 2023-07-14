
#! ############################################Importiere Module und Funktionen########################################################

import tkinter as tk
import csv
import mysql.connector
import schedule
import time
from tkinter import Tk, Button, Entry, Label
from tkinter.filedialog import asksaveasfilename
from datetime import datetime, timedelta


 #! ###########################################Aufruf Unterfunktionen Def###############################################################

#? def- Schreibe alle Daten aus Datenbank in ein Excelfile 
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
 
def button_DBSaveCurDay():
    db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database="ford1419_st2_eol"
    )
    cursor = db_connection.cursor()
    date = entry.get()

   
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





# Erstelle ein Fenster
fenster = tk.Tk()

# Definiere den Titel des Fensters
fenster.title("DB Collector")

# Definiere die Größe des Fensters
fenster.geometry("800x400")

# Textfeld
label = tk.Label(fenster, text='01') 
label.pack(side="bottom"  )

#Button Save alles
button_DB_save_all = tk.Button(fenster, text="SaveAll!" , command=button_DBSaveAll)
button_DB_save_all .config(width=20, height=3)
button_DB_save_all .place(x=20, y=50, )

#Button Save aktuellen Tag 
button_DB_save_cd = tk.Button(fenster, text="SaveDay!" , command=button_DBSaveCurDay)
button_DB_save_cd .config(width=20, height=3)
button_DB_save_cd .place(x=160, y=50, )

# Eingabefeld für das Datum hinzufügen
entry_label = Label(fenster, text="Datum (YYYY-MM-DD): ")
entry_label.pack()
entry = Entry(fenster)
entry.pack()


# Starte die Hauptschleife des Fensters
fenster.mainloop()
##########################################################################Fenster Config ende####################################################
