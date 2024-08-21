
import tkinter as tk
from DBConfig import Read_Config, Write_Config, DBSaveAll, DBSaveCurDay
from GUIConfig import HomeScreenConfig

# Funktion zum Schreiben der Konfigurationsdatei
def Button_write_DB_config(host, user, database):
    Write_Config(host, user, database, save_path_all_var.get(), save_path_day_var.get())

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

# Erstelle StringVars für die Pfade
save_path_all_var = tk.StringVar(value=save_path_all)
save_path_day_var = tk.StringVar(value=save_path_day)

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
    save_path_day_var
)

# Starte die Hauptschleife
Main_GUI.mainloop()