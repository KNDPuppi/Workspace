

import configparser
import os

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