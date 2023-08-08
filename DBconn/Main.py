
#! ############################################Importiere Module und Funktionen########################################################

import tkinter as tk


from DBConfig import Read_Config, Write_Config, DBSaveAll, DBSaveCurDay
from GUIConfig import HomeScreenConfig

#! ###########################################Aufruf Unterfunktionen Def###############################################################




def Button_write_DB_config(host, user, database): 
    Write_Config(host, user,database)

def Button_Save_all_data():
    VarTransIn_Read_Config = Read_Config()
    host = VarTransIn_Read_Config['t_host']
    user = VarTransIn_Read_Config['t_user']
    database = VarTransIn_Read_Config['t_database']

    DBSaveAll(host, user,database)
    
def Button_Save_CurrenDay(inputDay):  
    VarTransIn_Read_Config = Read_Config()
    host = VarTransIn_Read_Config['t_host']
    user = VarTransIn_Read_Config['t_user']
    database = VarTransIn_Read_Config['t_database']

    DBSaveCurDay(host, user, database, inputDay)
 
    
#! ########################################### GUI Aufruf und Hauptschleife###############################################################
# Öffne Homescreen
Main_GUI = tk.Tk()

VarTransIn_Read_Config = Read_Config()
host = VarTransIn_Read_Config['t_host']
user = VarTransIn_Read_Config['t_user']
database = VarTransIn_Read_Config['t_database']


HomeScreenConfig(Main_GUI, host, user, database,
                 Button_write_DB_config,
                 Button_Save_all_data,
                 Button_Save_CurrenDay
                 )




# Starte die Hauptschleife des Fensters
Main_GUI.mainloop()
##########################################################################Fenster Config ende####################################################
