import tkinter as tk
from tkinter import messagebox
from DBConfig import Read_Config, Write_Config, DBSaveAll, DBSaveCurDay
from GUIConfig import HomeScreenConfig
import threading
import time
import datetime

def Button_write_DB_config(host, user, database):
    Write_Config(host, user, database, save_path_all_var.get(), save_path_day_var.get(), scheduled_time_var.get())
    messagebox.showinfo("Info", "Datenbankkonfiguration gespeichert!")

def Button_Save_all_data():
    VarTransIn_Read_Config = Read_Config()
    host = VarTransIn_Read_Config['t_host']
    user = VarTransIn_Read_Config['t_user']
    database = VarTransIn_Read_Config['t_database']
    DBSaveAll(host, user, database, save_path_all_var.get())

def Button_Save_CurrenDay(inputDay):
    VarTransIn_Read_Config = Read_Config()
    host = VarTransIn_Read_Config['t_host']
    user = VarTransIn_Read_Config['t_user']
    database = VarTransIn_Read_Config['t_database']
    DBSaveCurDay(host, user, database, inputDay, save_path_day_var.get())

def scheduled_task():
    while True:
        now = datetime.datetime.now().time()
        current_time_str = now.strftime("%H:%M")
        if current_time_str == scheduled_time_str:
            VarTransIn_Read_Config = Read_Config()
            host = VarTransIn_Read_Config['t_host']
            user = VarTransIn_Read_Config['t_user']
            database = VarTransIn_Read_Config['t_database']
            inputDay = datetime.datetime.now().strftime("%Y-%m-%d")
            DBSaveCurDay(host, user, database, inputDay, save_path_day_var.get())
            time.sleep(60)  # Warten, um Mehrfachausführungen zu vermeiden
        else:
            time.sleep(1)  # Jede Sekunde prüfen

Main_GUI = tk.Tk()

VarTransIn_Read_Config = Read_Config()
host = VarTransIn_Read_Config['t_host']
user = VarTransIn_Read_Config['t_user']
database = VarTransIn_Read_Config['t_database']
save_path_all = VarTransIn_Read_Config['save_path_all']
save_path_day = VarTransIn_Read_Config['save_path_day']
scheduled_time_str = VarTransIn_Read_Config['scheduled_time']

save_path_all_var = tk.StringVar(value=save_path_all)
save_path_day_var = tk.StringVar(value=save_path_day)
scheduled_time_var = tk.StringVar(value=scheduled_time_str)

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

scheduler_thread = threading.Thread(target=scheduled_task, daemon=True)
scheduler_thread.start()

Main_GUI.mainloop()
