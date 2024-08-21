
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
        return {'t_host': '', 't_user': '', 't_database': '', 't_save_path_all': '', 't_save_path_day': ''}

    # Lese die Konfigurationsdatei
    config.read(config_file_path)

    # Versuche, die Konfigurationswerte zu lesen
    try:
        host = config.get('Database', 'host')
        user = config.get('Database', 'user')
        database = config.get('Database', 'database')
        save_path_all = config.get('Paths', 'save_path_all')
        save_path_day = config.get('Paths', 'save_path_day')
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        print(f"Fehler beim Lesen der Konfiguration: {e}")
        return {'t_host': '', 't_user': '', 't_database': '', 't_save_path_all': '', 't_save_path_day': ''}

    # Definiere zu übergebende Variablen
    transfer_variables = {
        't_host': host,
        't_user': user,
        't_database': database,
        't_save_path_all': save_path_all,
        't_save_path_day': save_path_day
    }

    return transfer_variables




#! Schreibe die aktuellen Zugangsdaten der Config Datenbank  
def Write_Config(host, user, database, save_path_all='', save_path_day=''):
    # Bestimme den Pfad zum Verzeichnis der Python-Datei
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Konstruiere den Pfad zur config.ini-Datei
    config_file_path = os.path.join(script_directory, 'config.ini')

    # Konfigurationsdatei erstellen oder laden
    config = configparser.ConfigParser()
    config.read(config_file_path)

    # Aktualisiere die Konfigurationsdaten
    config['Database'] = {
        'host': host,
        'user': user,
        'database': database
    }
    
    config['Paths'] = {
        'save_path_all': save_path_all,
        'save_path_day': save_path_day
    }

    # Konfigurationsdaten in die Datei schreiben
    with open(config_file_path, 'w') as config_file:
        config.write(config_file)



#! def- Schreibe alle Daten aus Datenbank in ein Excelfile (mit asksaveasfilename)  
def DBSaveAll(host, user, database, save_path):
    try:
        db_connection = mysql.connector.connect(
            host=host,
            user=user,
            database=database
        )
        cursor = db_connection.cursor()

        select_query = "SELECT * FROM prozessdaten"
        cursor.execute(select_query)
        results = cursor.fetchall()

        root = Tk()
        root.withdraw()

        # Dateiname definieren
        file_path = os.path.join(save_path, "DB_All.csv")

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
        try:
            cursor.close()
            db_connection.close()
        except:
            pass
        root.destroy()

def DBSaveCurDay(host, user, database, inputDay, save_path):
    try:
        db_connection = mysql.connector.connect(
            host=host,
            user=user,
            database=database
        )
        cursor = db_connection.cursor()

        select_query = "SELECT * FROM prozessdaten WHERE DATE(timestamp) = %s"
        cursor.execute(select_query, (inputDay,))
        results = cursor.fetchall()

        root = Tk()
        root.withdraw()

        # Dateiname definieren
        file_path = os.path.join(save_path, f"DB_Day_{inputDay}.csv")

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
        try:
            cursor.close()
            db_connection.close()
        except:
            pass
        root.destroy()