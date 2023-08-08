
#! ############################################Importiere Module und Funktionen  ############################################################
import tkinter as tk
import winreg

from tkinter import ttk, Entry, Label, Button


#! ############################################Importiere Module und Funktionen Ende ########################################################


def HomeScreenConfig(Main_GUI, host, user, database, Button_write_db_config):
         
   
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
    
    # Textfeld
    label = tk.Label(Main_GUI, text='01') 
    label.pack(side="bottom"  )

     # Erstelle einen Button
    button_trigger = Button(Main_GUI, text="Funktion im Hauptprogramm auslösen", command=Button_write_db_config)
    button_trigger.pack()  
    
        
    # Eingabefeld für das Datum hinzufügen
    entry_label = Label(Main_GUI, text="Datum (YYYY-MM-DD): ")
    entry_label.pack()
    entry = Entry(Main_GUI)
    entry.pack()

     # Eingabefeld für das host
    entry_host = Label(Main_GUI, text="Host ")
    entry_host.pack()
    entry_host = Entry(Main_GUI)
    entry_host.pack()

      # Eingabefeld für root
    entry_user = Label(Main_GUI, text="user ")
    entry_user.pack()
    entry_user = Entry(Main_GUI)
    entry_user.pack()

      # Eingabefeld für Database
    entry_db = Label(Main_GUI, text="database ")
    entry_db.pack()
    entry_db = Entry(Main_GUI)
    entry_db.pack()

          # Eingabefeld für root
    entry_pw = Label(Main_GUI, text="Password ")
    entry_pw.pack()
    entry_pw = Entry(Main_GUI)
    entry_pw.pack()
  

    entry_host.insert(0, host)  # Führe die Einfügung erst nach dem Lesen der Konfigurationswerte durch
    entry_user.insert(0, user)
    entry_db.insert(0, database)

    #defeniere zu übergebende Variablen
    transfer_variables = {
        't_host' : entry_host.get(),
        't_user' : entry_user.get(),
        't_database' : entry_db.ge()
    }

    return transfer_variables
