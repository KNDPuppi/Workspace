import configparser
import os
import mysql.connector
import csv
import datetime
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename, askdirectory

def Read_Config():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(script_directory, 'config.ini')

    config = configparser.ConfigParser()
    if not os.path.isfile(config_file_path):
        print(f"Konfigurationsdatei nicht gefunden: {config_file_path}")
        return {'t_host': '', 't_user': '', 't_database': '', 'save_path_all': '', 'save_path_day': '', 'scheduled_time': ''}

    config.read(config_file_path)

    try:
        host = config.get('Database', 'Host')
        user = config.get('Database', 'User')
        database = config.get('Database', 'Database')
        save_path_all = config.get('Settings', 'SavePathAll')
        save_path_day = config.get('Settings', 'SavePathDay')
        scheduled_time = config.get('Settings', 'ScheduledTime')
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        print(f"Fehler beim Lesen der Konfiguration: {e}")
        return {'t_host': '', 't_user': '', 't_database': '', 'save_path_all': '', 'save_path_day': '', 'scheduled_time': ''}

    transfer_variables = {
        't_host': host,
        't_user': user,
        't_database': database,
        'save_path_all': save_path_all,
        'save_path_day': save_path_day,
        'scheduled_time': scheduled_time
    }

    return transfer_variables

def Write_Config(host, user, database, save_path_all, save_path_day, scheduled_time):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(script_directory, 'config.ini')

    config = configparser.ConfigParser()
    config.read(config_file_path)

    config['Database'] = {
        'Host': host,
        'User': user,
        'Database': database
    }

    config['Settings'] = {
        'SavePathAll': save_path_all,
        'SavePathDay': save_path_day,
        'ScheduledTime': scheduled_time
    }

    with open(config_file_path, 'w') as config_file:
        config.write(config_file)

def DBSaveAll(host, user, database, save_path_all):
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

        # Erzeuge einen Dateinamen mit Zeitstempel
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(save_path_all, f"all_data_{timestamp}.csv")

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

def DBSaveCurDay(host, user, database, inputDay, save_path_day):
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

        # Erzeuge einen Dateinamen mit Datum und Zeitstempel
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(save_path_day, f"daily_data_{inputDay}_{timestamp}.csv")

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
