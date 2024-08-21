
import csv
import mysql.connector
import configparser
import os

from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

def Read_Config():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(script_directory, 'config.ini')

    config = configparser.ConfigParser()

    if not os.path.isfile(config_file_path):
        print(f"Konfigurationsdatei nicht gefunden: {config_file_path}")
        return {'t_host': '', 't_user': '', 't_database': '', 'scheduled_time': ''}

    config.read(config_file_path)

    try:
        host = config.get('Database', 'Host')
        user = config.get('Database', 'User')
        database = config.get('Database', 'Database')
        scheduled_time = config.get('Settings', 'ScheduledTime')
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        print(f"Fehler beim Lesen der Konfiguration: {e}")
        return {'t_host': '', 't_user': '', 't_database': '', 'scheduled_time': ''}

    return {'t_host': host, 't_user': user, 't_database': database, 'scheduled_time': scheduled_time}

def Write_Config(host, user, database, scheduled_time=None):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(script_directory, 'config.ini')

    config = configparser.ConfigParser()
    config.read(config_file_path)

    config['Database'] = {
        'Host': host,
        'User': user,
        'Database': database
    }

    if scheduled_time:
        if 'Settings' not in config:
            config['Settings'] = {}
        config['Settings']['ScheduledTime'] = scheduled_time

    with open(config_file_path, 'w') as config_file:
        config.write(config_file)

def DBSaveAll(host, user, database, file_path):
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

        if not file_path:
            root = Tk()
            root.withdraw()
            file_path = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Dateien", "*.csv")])
            if not file_path:
                return

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

def DBSaveCurDay(host, user, database, inputDay, file_path):
    try:
        db_connection = mysql.connector.connect(
            host=host,
            user=user,
            database=database
        )
        cursor = db_connection.cursor()
        date = inputDay

        select_query = "SELECT * FROM prozessdaten WHERE DATE(timestamp) = %s"
        cursor.execute(select_query, (date,))
        results = cursor.fetchall()

        if not file_path:
            root = Tk()
            root.withdraw()
            file_path = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Dateien", "*.csv")])
            if not file_path:
                return

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