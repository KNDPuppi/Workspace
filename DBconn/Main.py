import tkinter as tk
import datetime
from DBConfig import Read_Config, Write_Config, DBSaveAll, DBSaveCurDay
from GUIConfig import HomeScreenConfig

# Funktion zum Schreiben der Konfigurationsdatei
def Button_write_DB_config(host, user, database):
    Write_Config(host, user, database, save_path_all_var.get(), save_path_day_var.get(), scheduled_time_var.get())

# Funktion zum Speichern aller Daten
def Button_Save_all_data():
    VarTransIn_Read_Config = Read_Config()
    host = VarTransIn_Read_Config['t_host']
    user = VarTransIn_Read_Config['t_user']
    database = VarTransIn_Read_Config['t_database']
    DBSaveAll(host, user, database, save_path_all_var.get())

# Funktion zum Speichern der Daten eines bestimmten Tages
def Button_Save_CurrenDay(inputDay):
    VarTransIn_Read_Config = Read_Config()
    host = VarTransIn_Read_Config['t_host']
    user = VarTransIn_Read_Config['t_user']
    database = VarTransIn_Read_Config['t_database']
    DBSaveCurDay(host, user, database, inputDay, save_path_day_var.get())

# Erstelle das Hauptfenster
Main_GUI = tk.Tk()

# Lese die Konfiguration
VarTransIn_Read_Config = Read_Config()
host = VarTransIn_Read_Config['t_host']
user = VarTransIn_Read_Config['t_user']
database = VarTransIn_Read_Config['t_database']
save_path_all = VarTransIn_Read_Config['save_path_all']
save_path_day = VarTransIn_Read_Config['save_path_day']
scheduled_time_str = VarTransIn_Read_Config['scheduled_time']

# Bereinige und parse den Zeitstring
def clean_time_string(time_string):
    return time_string.split()[0]  # Nimmt nur den ersten Teil des Strings, falls zusätzliche Daten vorhanden sind

try:
    scheduled_time_str = clean_time_string(scheduled_time_str)
    scheduled_time = datetime.datetime.strptime(scheduled_time_str, "%H:%M").time()
except ValueError as e:
    print(f"Fehler beim Parsen der Zeit: {e}")
    scheduled_time = None

# Erstelle StringVars für die Pfade
save_path_all_var = tk.StringVar(value=save_path_all)
save_path_day_var = tk.StringVar(value=save_path_day)
scheduled_time_var = tk.StringVar(value=scheduled_time_str)

# Rufe die GUI-Konfiguration auf
HomeScreenConfig(
    Main_GUI, 
    host, 
    user, 
    database,
    Button_write_DB_config,
    Button_Save_all_data,
    Button_Save_CurrenDay,
    save_path_all_var,
    save_path_day_var,
    scheduled_time_var
)

# Starte die Hauptschleife
Main_GUI.mainloop()
