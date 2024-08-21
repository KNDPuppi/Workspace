
import tkinter as tk
from DBConfig import Read_Config, Write_Config, DBSaveAll, DBSaveCurDay
from GUIConfig import HomeScreenConfig

def Button_write_DB_config(host, user, database): 
    VarTransIn_Read_Config = Read_Config()
    Write_Config(host, user, database, VarTransIn_Read_Config['t_save_path_all'], VarTransIn_Read_Config['t_save_path_day'])

def Button_Save_all_data():
    VarTransIn_Read_Config = Read_Config()
    host = VarTransIn_Read_Config['t_host']
    user = VarTransIn_Read_Config['t_user']
    database = VarTransIn_Read_Config['t_database']
    save_path_all = VarTransIn_Read_Config['t_save_path_all']

    DBSaveAll(host, user, database, save_path_all)

def Button_Save_CurrenDay(inputDay):  
    VarTransIn_Read_Config = Read_Config()
    host = VarTransIn_Read_Config['t_host']
    user = VarTransIn_Read_Config['t_user']
    database = VarTransIn_Read_Config['t_database']
    save_path_day = VarTransIn_Read_Config['t_save_path_day']

    DBSaveCurDay(host, user, database, inputDay, save_path_day)

Main_GUI = tk.Tk()

VarTransIn_Read_Config = Read_Config()
host = VarTransIn_Read_Config['t_host']
user = VarTransIn_Read_Config['t_user']
database = VarTransIn_Read_Config['t_database']
save_path_all = VarTransIn_Read_Config['t_save_path_all']
save_path_day = VarTransIn_Read_Config['t_save_path_day']

HomeScreenConfig(Main_GUI, host, user, database, save_path_all, save_path_day,
                 Button_write_DB_config,
                 Button_Save_all_data,
                 Button_Save_CurrenDay
                 )

Main_GUI.mainloop()