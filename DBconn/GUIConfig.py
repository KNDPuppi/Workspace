import tkinter as tk
from tkinter import ttk
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
            import winreg
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

        # Frame für Datenbankkonfiguration
        db_frame = ttk.LabelFrame(Main_GUI, text="Datenbankkonfiguration", padding=(10, 10))
        db_frame.grid(row=0, column=0, padx=20, pady=10, sticky='ew')

        ttk.Label(db_frame, text="Host:").grid(row=0, column=0, sticky='w')
        host_entry = ttk.Entry(db_frame, width=40)
        host_entry.insert(0, host)
        host_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(db_frame, text="Benutzername:").grid(row=1, column=0, sticky='w')
        user_entry = ttk.Entry(db_frame, width=40)
        user_entry.insert(0, user)
        user_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(db_frame, text="Datenbank:").grid(row=2, column=0, sticky='w')
        db_entry = ttk.Entry(db_frame, width=40)
        db_entry.insert(0, database)
        db_entry.grid(row=2, column=1, padx=10, pady=5)

        Button_save_DB_config = ttk.Button(db_frame, text="Konfiguration speichern", command=lambda: button_function_WrDB(host_entry.get(), user_entry.get(), db_entry.get()))
        Button_save_DB_config.grid(row=3, column=0, columnspan=2, pady=10)

        # Frame für Daten speichern
        data_frame = ttk.LabelFrame(Main_GUI, text="Daten speichern", padding=(10, 10))
        data_frame.grid(row=1, column=0, padx=20, pady=10, sticky='ew')

        Button_Save_all = ttk.Button(data_frame, text="Alle Daten speichern", command=button_function_Save_all)
        Button_Save_all.grid(row=0, column=0, columnspan=2, pady=5)

        ttk.Label(data_frame, text="Wähle Datum:").grid(row=1, column=0, sticky='w')
        date_entry = DateEntry(data_frame, date_pattern='yyyy-mm-dd', width=12)
        date_entry.grid(row=1, column=1, padx=10, pady=5)

        Button_Save_Day = ttk.Button(data_frame, text="Tagesdaten speichern", command=lambda: button_function_Save_Day(date_entry.get()))
        Button_Save_Day.grid(row=2, column=0, columnspan=2, pady=5)

        # Frame für Pfade und automatische Ausführung
        path_frame = ttk.LabelFrame(Main_GUI, text="Pfade und automatische Ausführung", padding=(10, 10))
        path_frame.grid(row=2, column=0, padx=20, pady=10, sticky='ew')

        ttk.Label(path_frame, text="Pfad für alle Daten:").grid(row=0, column=0, sticky='w')
        save_path_all_entry = ttk.Entry(path_frame, textvariable=save_path_all_var, width=30)
        save_path_all_entry.grid(row=0, column=1, padx=10, pady=5)

        Button_save_path_all = ttk.Button(path_frame, text="Durchsuchen", command=lambda: browse_directory(save_path_all_var))
        Button_save_path_all.grid(row=0, column=2, padx=5, pady=5)

        ttk.Label(path_frame, text="Pfad für Tagesdaten:").grid(row=1, column=0, sticky='w')
        save_path_day_entry = ttk.Entry(path_frame, textvariable=save_path_day_var, width=30)
        save_path_day_entry.grid(row=1, column=1, padx=10, pady=5)

        Button_save_path_day = ttk.Button(path_frame, text="Durchsuchen", command=lambda: browse_directory(save_path_day_var))
        Button_save_path_day.grid(row=1, column=2, padx=5, pady=5)

        ttk.Label(path_frame, text="Automatische Ausführung (HH:MM):").grid(row=2, column=0, sticky='w')
        scheduled_time_entry = ttk.Entry(path_frame, textvariable=scheduled_time_var, width=10)
        scheduled_time_entry.grid(row=2, column=1, padx=10, pady=5)

        # Update der Fenstergröße, um sicherzustellen, dass alle Elemente passen
        Main_GUI.update_idletasks()
        window_width = Main_GUI.winfo_reqwidth()
        window_height = Main_GUI.winfo_reqheight()
        Main_GUI.geometry(f'{window_width}x{window_height}')

    except Exception as e:
        print(f"Fehler bei der GUI-Konfiguration: {e}")

def browse_directory(path_variable):
    directory = askdirectory()
    if directory:
        path_variable.set(directory)
