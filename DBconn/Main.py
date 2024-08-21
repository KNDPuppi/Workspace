
import tkinter as tk
from tkinter import filedialog

from DBConfig import Read_Config, Write_Config, DBSaveAll, DBSaveCurDay
from GUIConfig import HomeScreenConfig

# Globaler Pfad für den Speicherort der CSV-Datei
save_path = ""

def Button_write_DB_config(host, user, database): 
    Write_Config(host, user, database)

def Button_Save_all_data():
    global save_path
    VarTransIn_Read_Config = Read_Config()
    host = VarTransIn_Read_Config['t_host']
    user = VarTransIn_Read_Config['t_user']
    database = VarTransIn_Read_Config['t_database']

    if not save_path:
        print("Speicherpfad ist nicht gesetzt.")
        return

    DBSaveAll(host, user, database, save_path)
    
def Button_Save_CurrenDay(inputDay):  
    VarTransIn_Read_Config = Read_Config()
    host = VarTransIn_Read_Config['t_host']
    user = VarTransIn_Read_Config['t_user']
    database = VarTransIn_Read_Config['t_database']

    DBSaveCurDay(host, user, database, inputDay)

def Button_Set_Save_Path():
    global save_path
    save_path = filedialog.askdirectory()
    if save_path:
        save_path_label.config(text=f"Save Path: {save_path}")

# Öffne Homescreen
Main_GUI = tk.Tk()

VarTransIn_Read_Config = Read_Config()
host = VarTransIn_Read_Config['t_host']
user = VarTransIn_Read_Config['t_user']
database = VarTransIn_Read_Config['t_database']

# Erstelle das Label-Widget, aber initial nicht zugewiesen
save_path_label = tk.Label()

# Übergib die Label-Variable an die GUIConfig-Funktion
save_path_label = HomeScreenConfig(Main_GUI, host, user, database,
                                   Button_write_DB_config,
                                   Button_Save_all_data,
                                   Button_Save_CurrenDay,
                                   Button_Set_Save_Path)

# Starte die Hauptschleife des Fensters
Main_GUI.mainloop()