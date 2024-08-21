import tkinter as tk
import winreg
from tkinter import ttk, Label, Button, Toplevel
from tkinter.filedialog import askdirectory
from tkcalendar import DateEntry

def HomeScreenConfig(Main_GUI, host, user, database,
                     button_function_WrDB,
                     button_function_Save_all,
                     button_function_Save_Day,
                     save_path_all_var,
                     save_path_day_var,
                     scheduled_time_var):
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
            style.theme_use(themename="default")

        Main_GUI.title("FTS-DB")

        # GUI-Größe und Position
        window_width = 450
        window_height = 300
        screen_width = Main_GUI.winfo_screenwidth()
        screen_height = Main_GUI.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        Main_GUI.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        Label(Main_GUI, text="Host:").grid(row=0, column=0, sticky='w')
        Label(Main_GUI, text="Benutzername:").grid(row=1, column=0, sticky='w')
        Label(Main_GUI, text="Datenbank:").grid(row=2, column=0, sticky='w')

        host_entry = ttk.Entry(Main_GUI)
        host_entry.insert(0, host)
        host_entry.grid(row=0, column=1, padx=10, pady=5)

        user_entry = ttk.Entry(Main_GUI)
        user_entry.insert(0, user)
        user_entry.grid(row=1, column=1, padx=10, pady=5)

        db_entry = ttk.Entry(Main_GUI)
        db_entry.insert(0, database)
        db_entry.grid(row=2, column=1, padx=10, pady=5)

        Button_save_DB_config = ttk.Button(Main_GUI, text="Write Config", command=lambda: button_function_WrDB(host_entry.get(), user_entry.get(), db_entry.get()))
        Button_save_DB_config.grid(row=3, column=0, columnspan=2, pady=10)

        # Speichern aller Daten
        Button_Save_all = ttk.Button(Main_GUI, text="Save DB All", command=button_function_Save_all)
        Button_Save_all.grid(row=4, column=0, columnspan=2, pady=5)

        # Speichern der Tagesdaten
        Label(Main_GUI, text="Wähle Datum:").grid(row=5, column=0, sticky='w')
        date_entry = DateEntry(Main_GUI, date_pattern='yyyy-mm-dd')
        date_entry.grid(row=5, column=1, padx=10, pady=5)

        Button_Save_Day = ttk.Button(Main_GUI, text="Save DB Day", command=lambda: button_function_Save_Day(date_entry.get()))
        Button_Save_Day.grid(row=6, column=0, columnspan=2, pady=5)

        # Pfad für alle Daten
        Label(Main_GUI, text="Pfad für alle Daten:").grid(row=7, column=0, sticky='w')
        save_path_all_entry = ttk.Entry(Main_GUI, textvariable=save_path_all_var, width=30)
        save_path_all_entry.grid(row=7, column=1, padx=10, pady=5)

        Button_save_path_all = ttk.Button(Main_GUI, text="Browse", command=lambda: browse_directory(save_path_all_var))
        Button_save_path_all.grid(row=7, column=2, padx=5, pady=5)

        # Pfad für Tagesdaten
        Label(Main_GUI, text="Pfad für Tagesdaten:").grid(row=8, column=0, sticky='w')
        save_path_day_entry = ttk.Entry(Main_GUI, textvariable=save_path_day_var, width=30)
        save_path_day_entry.grid(row=8, column=1, padx=10, pady=5)

        Button_save_path_day = ttk.Button(Main_GUI, text="Browse", command=lambda: browse_directory(save_path_day_var))
        Button_save_path_day.grid(row=8, column=2, padx=5, pady=5)

        # Automatische Ausführungszeit
        Label(Main_GUI, text="Automatische Ausführung (HH:MM):").grid(row=9, column=0, sticky='w')
        scheduled_time_entry = ttk.Entry(Main_GUI, textvariable=scheduled_time_var, width=10)
        scheduled_time_entry.grid(row=9, column=1, padx=10, pady=5)

    except Exception as e:
        print(f"Fehler bei der GUI-Konfiguration: {e}")

def browse_directory(path_variable):
    directory = askdirectory()
    if directory:
        path_variable.set(directory)
