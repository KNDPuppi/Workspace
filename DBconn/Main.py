
import tkinter as tk
from DBConfig import Read_Config, Write_Config, DBSaveAll, DBSaveCurDay
from GUIConfig import HomeScreenConfig

# Globale Variablen für Speicherpfade
save_path_all = ""
save_path_day = ""

def Button_write_DB_config(host, user, database): 
    Write_Config(host, user, database)

def Button_Save_all_data():
    global save_path_all
    VarTransIn_Read_Config = Read_Config()
    host = VarTransIn_Read_Config['t_host']
    user = VarTransIn_Read_Config['t_user']
    database = VarTransIn_Read_Config['t_database']

    if save_path_all:
        DBSaveAll(host, user, database, save_path_all)  # Pfad übergeben
    else:
        print("Speicherpfad für 'Save All' ist nicht festgelegt.")

def Button_Save_CurrenDay(inputDay):  
    global save_path_day
    VarTransIn_Read_Config = Read_Config()
    host = VarTransIn_Read_Config['t_host']
    user = VarTransIn_Read_Config['t_user']
    database = VarTransIn_Read_Config['t_database']

    if save_path_day:
        DBSaveCurDay(host, user, database, inputDay, save_path_day)  # Pfad übergeben
    else:
        print("Speicherpfad für 'Save Day' ist nicht festgelegt.")

def Button_Set_Save_Path_All():
    global save_path_all
    save_path_all = askdirectory()  # Pfad festlegen

    if save_path_label_all:
        save_path_label_all.config(text=f"Save Path All: {save_path_all}")

def Button_Set_Save_Path_Day():
    global save_path_day
    save_path_day = askdirectory()  # Pfad festlegen

    if save_path_label_day:
        save_path_label_day.config(text=f"Save Path Day: {save_path_day}")

# Öffne Homescreen
Main_GUI = tk.Tk()

VarTransIn_Read_Config = Read_Config()
host = VarTransIn_Read_Config['t_host']
user = VarTransIn_Read_Config['t_user']
database = VarTransIn_Read_Config['t_database']

save_path_label_all, save_path_label_day = HomeScreenConfig(Main_GUI, host, user, database,
                 Button_write_DB_config,
                 Button_Save_all_data,
                 Button_Save_CurrenDay,
                 Button_Set_Save_Path_All,
                 Button_Set_Save_Path_Day)

# Starte die Hauptschleife des Fensters
Main_GUI.mainloop()