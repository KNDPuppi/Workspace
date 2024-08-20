
#! ############################################Importiere Module und Funktionen  ############################################################
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

    # Erstelle ein ConfigParser-Objekt
    config = configparser.ConfigParser()

    # Überprüfe, ob die Konfigurationsdatei existiert
    if not os.path.isfile(config_file_path):
        print(f"Konfigurationsdatei nicht gefunden: {config_file_path}")
        return {'t_host': '', 't_user': '', 't_database': ''}

    # Lese die Konfigurationsdatei
    config.read(config_file_path)

    # Versuche, die Konfigurationswerte zu lesen
    try:
        host = config.get('Database', 'Host')
        user = config.get('Database', 'User')
        database = config.get('Database', 'Database')
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        print(f"Fehler beim Lesen der Konfiguration: {e}")
        return {'t_host': '', 't_user': '', 't_database': ''}

    # Definiere zu übergebende Variablen
    transfer_variables = {
        't_host': host,
        't_user': user,
        't_database': database
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
    try:
        # Stelle die Verbindung zur Datenbank her
        db_connection = mysql.connector.connect(
            host=host,
            user=user,
            database=database
        )
        cursor = db_connection.cursor()

        # Führe die SQL-Abfrage aus
        select_query = "SELECT * FROM prozessdaten"
        cursor.execute(select_query)
        results = cursor.fetchall()

        # Öffne einen Dialog zum Speichern der CSV-Datei
        root = Tk()
        root.withdraw()

        file_path = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Dateien", "*.csv")])
        if not file_path:
            return  # Benutzer hat den Datei-Speicher-Dialog abgebrochen

        # Schreibe die Daten in die CSV-Datei
        with open(file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            column_names = [i[0] for i in cursor.description]
            csv_writer.writerow(column_names)
            csv_writer.writerows(results)

    except mysql.connector.Error as err:
        print(f"Fehler bei der Datenbankabfrage: {err}")
    except IOError as e:
        print(f"Fehler beim Schreiben der Datei: {e}")
    finally:
        # Schließe Verbindung und Cursor
        try:
            cursor.close()
            db_connection.close()
        except:
            pass
        # Schließe das Wurzelfenster
        root.destroy()



#! def- Schreibe alle Daten eines Tages in ein Excelfile (mit asksaveasfilename)
def DBSaveCurDay(host, user, database, inputDay):
    try:
        # Stelle die Verbindung zur Datenbank her
        db_connection = mysql.connector.connect(
            host=host,
            user=user,
            database=database
        )
        cursor = db_connection.cursor()
        date = inputDay

        # Führe die SQL-Abfrage aus
        select_query = "SELECT * FROM prozessdaten WHERE DATE(timestamp) = %s"
        cursor.execute(select_query, (date,))
        results = cursor.fetchall()

        # Öffne einen Dialog zum Speichern der CSV-Datei
        root = Tk()
        root.withdraw()

        file_path = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Dateien", "*.csv")])
        if not file_path:
            return  # Benutzer hat den Datei-Speicher-Dialog abgebrochen

        # Schreibe die Daten in die CSV-Datei
        with open(file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            column_names = [i[0] for i in cursor.description]
            csv_writer.writerow(column_names)
            csv_writer.writerows(results)

    except mysql.connector.Error as err:
        print(f"Fehler bei der Datenbankabfrage: {err}")
    except IOError as e:
        print(f"Fehler beim Schreiben der Datei: {e}")
    finally:
        # Schließe Verbindung und Cursor
        try:
            cursor.close()
            db_connection.close()
        except:
            pass
        # Schließe das Wurzelfenster
        root.destroy()