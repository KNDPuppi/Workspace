
#! ############################################Importiere Module und Funktionen  ############################################################
import tkinter as tk
import winreg

from tkinter import ttk, Entry, Label, Button
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
    Main_GUI.geometry("800x400")

    frame1 = tk.Frame(Main_GUI)
    frame1.pack()

    frame2 = tk.Frame(Main_GUI)
    frame2.pack()
          
        
    # Eingabefeld für das Datum hinzufügen
    entry_Date = DateEntry(frame1, date_pattern="yyyy-mm-dd")
    entry_Date.pack()



     # Eingabefeld für das host
    entry_host = Label(frame2, text="Host ")
    entry_host.pack()
    entry_host = Entry(frame2)
    entry_host.pack()

      # Eingabefeld für root
    entry_user = Label(frame2, text="user ")
    entry_user.pack()
    entry_user = Entry(frame2)
    entry_user.pack()

      # Eingabefeld für Database
    entry_db = Label(frame2, text="database ")
    entry_db.pack()
    entry_db = Entry(frame2)
    entry_db.pack()

          # Eingabefeld für root
    entry_pw = Label(frame2, text="Password ")
    entry_pw.pack()
    entry_pw = Entry(master=frame2)
    entry_pw.pack()
  

    entry_host.insert(0, host)  # Führe die Einfügung erst nach dem Lesen der Konfigurationswerte durch
    entry_user.insert(0, user)
    entry_db.insert(0, database)







    #!################################################ Eingabe #####################################################################################

    # Button Speichere DB_Configdaten
    button_writeDB = Button(Main_GUI, text="Save DB Config", command=lambda: button_function_WrDB(entry_host.get(), entry_user.get(), entry_db.get()))
    button_writeDB.pack()  

    # Button SAVE All
    button_SaveDB_ALL = Button(Main_GUI, text="Save DB ALL", command=button_function_Save_all)
    button_SaveDB_ALL.pack()  

    # Button SAVE Day
    button_SaveDB_Day = Button(Main_GUI, text="Save DB Day", command=lambda: button_function_Save_Day(entry_Date.get()))
    button_SaveDB_Day.pack() 
   