
#! ############################################Importiere Module und Funktionen  ############################################################
import tkinter as tk
import winreg

from tkinter import ttk, Entry, Label


#! ############################################Importiere Module und Funktionen Ende ########################################################


def HomeScreenConfig(Main_GUI, host, user, database):
         
   
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
    entry_root = Label(Main_GUI, text="root ")
    entry_root.pack()
    entry_root = Entry(Main_GUI)
    entry_root.pack()

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
    entry_root.insert(0, user)
    entry_db.insert(0, database)