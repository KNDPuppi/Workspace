


import csv
import mysql.connector
import configparser
import os

from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

#! Lese aktuelle Datenbank daten
def Read_Config():
  
    
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

    #defeniere zu übergebende Variablen
    transfer_variables = {
        't_host' : host,
        't_user' : user,
        't_database' : database 
    }

    return transfer_variables





#! Schreibe die aktuellen Zugangsdaten der Config Datenbank  
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




#! def- Schreibe alle Daten aus Datenbank in ein Excelfile (mit asksaveasfilename)  
def DBSaveAll(host, user, database):
    
    
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