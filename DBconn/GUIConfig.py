
#! ############################################Importiere Module und Funktionen  ############################################################
import tkinter as tk
import winreg

from tkinter import ttk, Entry, Label, Button, Toplevel
from tkcalendar import DateEntry

#! ############################################Importiere Module und Funktionen Ende ########################################################


def HomeScreenConfig(Main_GUI, host, user, database,
                     button_function_WrDB,
                     button_function_Save_all,
                     button_function_Save_Day):
         
   
    style = ttk.Style(Main_GUI)

    # Ermittle das aktuelle Fensterdesign von Windows
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
    theme = winreg.QueryValueEx(key, "AppsUseLightTheme")[0]

    # Passe das Thema an das Betriebssystem an
    if theme == 0:
        style.theme_use(themename="clam")
    else:
        style.theme_use(themename="dark")

    Main_GUI.title("DB Collector")

    frame = tk.Frame(Main_GUI)
    frame.pack(fill="both", expand=True)

    user_frame_1 = tk.LabelFrame(frame, text="User Information")
    user_frame_1.grid(row=0, column=0, padx=20, pady=10, sticky="news")
     
        # Eingabefeld für das Datum hinzufügen
    entry_Date = DateEntry(user_frame_1, date_pattern="yyyy-mm-dd" , width=20 )
    entry_Date.grid(row=0, column=1)

    # Eingabefeld für das host
    entry_host_label = Label(user_frame_1, text="Host")
    entry_host_label.grid(row=1, column=0)
    entry_host = ttk.Entry(user_frame_1,  width=23, justify="right")
    entry_host.grid(row=1, column=1)

    # Eingabefeld für user
    entry_user_label = Label(user_frame_1, text="User")
    entry_user_label.grid(row=2, column=0)
    entry_user = ttk.Entry(user_frame_1, width=23, justify="right")
    entry_user.grid(row=2, column=1)

    # Eingabefeld für Database
    entry_db_label = Label(user_frame_1, text="Database")
    entry_db_label.grid(row=3, column=0)
    entry_db =ttk.Entry(user_frame_1, width=23, justify="right" )
    entry_db.grid(row=3, column=1)

    entry_host.insert(0, host)
    entry_user.insert(0, user)
    entry_db.insert(0, database)



  #!################################################ Eingabe #####################################################################################

# Buttons
    button_width = 20  # Ändere die Breite nach Bedarf
    button_height = 4

    
    button_writeDB = Button(user_frame_1, text="Save DB Config", width=button_width,  height=button_height, command=lambda: button_function_WrDB(entry_host.get(), entry_user.get(), entry_db.get()))
    button_writeDB.grid(row=4, column=0, columnspan=2, sticky="e")

    button_SaveDB_ALL = Button(user_frame_1, text="Save DB ALL", width=button_width, height=button_height, command=button_function_Save_all)
    button_SaveDB_ALL.grid(row=5, column=0, columnspan=2, sticky="e")

    button_SaveDB_Day = Button(user_frame_1, text="Save DB Day", width=button_width, height=button_height, command=lambda: button_function_Save_Day(entry_Date.get()))
    button_SaveDB_Day.grid(row=6, column=0, columnspan=2,  sticky="e")

    button_SaveDB_Day = Button(user_frame_1, text="DB Conbfig", width=button_width, height=button_height, command=lambda: open_database_settings(Main_GUI))
    button_SaveDB_Day.grid(row=7, column=0, columnspan=2,  sticky="e")
    
    for widget in user_frame_1.winfo_children():
        widget.grid_configure(padx=20, pady=5)







#! ########################################### Neues Fenster Toplevel ###############################################################   
def open_database_settings(Main_GUI):
    db_settings_window = Toplevel(Main_GUI)
    db_settings_window.title("Database Settings")
            
#! ########################################### GUI Aufruf und Hauptschleife###############################################################

    

  
