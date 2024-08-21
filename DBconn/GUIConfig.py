import tkinter as tk
import winreg
from tkinter import ttk, Entry, Label, Button, Toplevel
from tkinter.filedialog import askdirectory
from tkcalendar import DateEntry
from datetime import datetime, timedelta
import threading
import time

def HomeScreenConfig(Main_GUI, host, user, database,
                     button_function_WrDB,
                     button_function_Save_all,
                     button_function_Save_Day,
                     save_path_all_var,
                     save_path_day_var,
                     time_entry_var):  # Neuer Parameter für die Uhrzeit
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
        labels_and_entries = [
            ("Host", entry_host := ttk.Entry(user_frame_1, width=23, justify="right")),
            ("User", entry_user := ttk.Entry(user_frame_1, width=23, justify="right")),
            ("Database", entry_db := ttk.Entry(user_frame_1, width=23, justify="right")),
            ("Time", entry_time := ttk.Entry(user_frame_1, width=23, justify="right"))  # Neues Eingabefeld für die Zeit
        ]

        for i, (label_text, entry) in enumerate(labels_and_entries, start=1):
            Label(user_frame_1, text=label_text).grid(row=i, column=0)
            entry.grid(row=i, column=1)
            entry.insert(0, locals()[f"entry_{label_text.lower()}"])

        # Zeige die gespeicherten Pfade an
        Label(user_frame_1, text="Save Path All").grid(row=8, column=0)
        save_path_all_label = Label(user_frame_1, textvariable=save_path_all_var, fg="gray")
        save_path_all_label.grid(row=8, column=1)

        Label(user_frame_1, text="Save Path Day").grid(row=9, column=0)
        save_path_day_label = Label(user_frame_1, textvariable=save_path_day_var, fg="gray")
        save_path_day_label.grid(row=9, column=1)

        Label(user_frame_1, text="Scheduled Time").grid(row=10, column=0)  # Neues Label für die Zeit
        entry_time.grid(row=10, column=1)  # Neues Eingabefeld für die Zeit

        # Buttons
        button_width = 20  # Ändere die Breite nach Bedarf
        button_height = 4

        Button(user_frame_1, text="Save DB Config", width=button_width, height=button_height,
               command=lambda: button_function_WrDB(entry_host.get(), entry_user.get(), entry_db.get(), entry_time.get())).grid(row=4, column=0, columnspan=2, sticky="e")

        Button(user_frame_1, text="Save DB ALL", width=button_width, height=button_height,
               command=lambda: button_function_Save_all()).grid(row=5, column=0, columnspan=2, sticky="e")

        Button(user_frame_1, text="Save DB Day", width=button_width, height=button_height,
               command=lambda: button_function_Save_Day(entry_Date.get())).grid(row=6, column=0, columnspan=2, sticky="e")

        Button(user_frame_1, text="DB Config", width=button_width, height=button_height,
               command=lambda: open_database_settings(Main_GUI)).grid(row=7, column=0, columnspan=2, sticky="e")

        for widget in user_frame_1.winfo_children():
            widget.grid_configure(padx=20, pady=5)
    except Exception as e:
        print(f"Fehler beim Erstellen der GUI: {e}")

def open_database_settings(Main_GUI):
    db_settings_window = Toplevel(Main_GUI)
    db_settings_window.title("Database Settings")