
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
    try:
        style = ttk.Style(Main_GUI)

        # Ermittle das aktuelle Fensterdesign von Windows
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
            theme = winreg.QueryValueEx(key, "AppsUseLightTheme")[0]
        except FileNotFoundError:
            print("Fehler beim Abrufen des Windows-Themes.")
            theme = 1  # Standardwert (Dunkelmodus)

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
        entry_Date = DateEntry(user_frame_1, date_pattern="yyyy-mm-dd", width=20)
        entry_Date.grid(row=0, column=1)

        # Eingabefelder
        entry_host = ttk.Entry(user_frame_1, width=23, justify="right")
        entry_user = ttk.Entry(user_frame_1, width=23, justify="right")
        entry_db = ttk.Entry(user_frame_1, width=23, justify="right")

        entries = {
            "Host": entry_host,
            "User": entry_user,
            "Database": entry_db
        }

        for i, (label_text, entry) in enumerate(entries.items(), start=1):
            Label(user_frame_1, text=label_text).grid(row=i, column=0)
            entry.grid(row=i, column=1)
            entry.insert(0, locals().get(f"{label_text.lower()}"))

        # Buttons
        button_width = 20  # Ändere die Breite nach Bedarf
        button_height = 4

        Button(user_frame_1, text="Save DB Config", width=button_width, height=button_height,
               command=lambda: button_function_WrDB(entry_host.get(), entry_user.get(), entry_db.get())).grid(row=4, column=0, columnspan=2, sticky="e")

        Button(user_frame_1, text="Save DB ALL", width=button_width, height=button_height,
               command=button_function_Save_all).grid(row=5, column=0, columnspan=2, sticky="e")

        Button(user_frame_1, text="Save DB Day", width=button_width, height=button_height,
               command=lambda: button_function_Save_Day(entry_Date.get())).grid(row=6, column=0, columnspan=2, sticky="e")

        Button(user_frame_1, text="DB Config", width=button_width, height=button_height,
               command=lambda: open_database_settings(Main_GUI)).grid(row=7, column=0, columnspan=2, sticky="e")

        for widget in user_frame_1.winfo_children():
            widget.grid_configure(padx=20, pady=5)
    except Exception as e:
        print(f"Fehler beim Erstellen der GUI: {e}")

#! ########################################### Neues Fenster Toplevel ###############################################################   
def open_database_settings(Main_GUI):
    db_settings_window = Toplevel(Main_GUI)
    db_settings_window.title("Database Settings")
    # Hier kannst du weitere GUI-Elemente für die Datenbankkonfiguration hinzufügen

#! ########################################### GUI Aufruf und Hauptschleife###############################################################
