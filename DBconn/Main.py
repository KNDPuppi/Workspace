import tkinter as tk
from tkinter import messagebox
from DBConfig import Read_Config, Write_Config, DBSaveAll, DBSaveCurDay
from GUIConfig import HomeScreenConfig
import threading
import time
import datetime

# Funktion zum Schreiben der Konfigurationsdatei
def Button_write_DB_config(host, user, database):
    Write_Config(host, user, database, save_path_all_var.get(), save_path_day_var.get(), scheduled_time_var.get())
    messagebox.showinfo("Info", "Datenbankkonfiguration gespeichert!")

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

# Funktion für die automatische Ausführung
def scheduled_task():
    while True:
        now = datetime.datetime.now().time()
        if now.strftime("%H:%M") == scheduled_time_str:
            VarTransIn_Read_Config = Read_Config()
            host = VarTransIn_Read_Config['t_host']
            user = VarTransIn_Read_Config['t_user']
            database = VarTransIn_Read_Config['t_database']
            inputDay = datetime.datetime.now().strftime("%Y-%m-%d")
            DBSaveCurDay(host, user, database, inputDay, save_path_day_var.get())
            time.sleep(60)  # Warten, um Mehrfachausführungen zu vermeiden
        time.sleep(1)  # Jede Sekunde prüfen

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

# Erstelle StringVars für die Pfade und die Zeit
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

# Starte den Scheduler in einem separaten Thread
scheduler_thread = threading.Thread(target=scheduled_task, daemon=True)
scheduler_thread.start()

# Starte die Hauptschleife
Main_GUI.mainloop()
