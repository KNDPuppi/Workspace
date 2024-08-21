import tkinter as tk
from tkinter import ttk, Label, Button, Toplevel
from tkinter.filedialog import askdirectory
from tkcalendar import DateEntry
import winreg

def HomeScreenConfig(Main_GUI, host, user, database,
                     button_function_WrDB,
                     button_function_Save_all,
                     button_function_Save_Day,
                     button_function_SetSavePath):
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

        # Eingabefelder für Host, User und Database
        entry_host = ttk.Entry(user_frame_1, width=23, justify="right")
        entry_user = ttk.Entry(user_frame_1, width=23, justify="right")
        entry_db = ttk.Entry(user_frame_1, width=23, justify="right")

        # Setze die initialen Werte
        entry_host.insert(0, host)
        entry_user.insert(0, user)
        entry_db.insert(0, database)

        # Labels und Eingabefelder in der GUI platzieren
        Label(user_frame_1, text="Host").grid(row=1, column=0)
        entry_host.grid(row=1, column=1)

        Label(user_frame_1, text="User").grid(row=2, column=0)
        entry_user.grid(row=2, column=1)

        Label(user_frame_1, text="Database").grid(row=3, column=0)
        entry_db.grid(row=3, column=1)

        # Neuer Button für den Speicherort
        button_set_save_path = Button(user_frame_1, text="Set Save Path", width=20, height=4, command=button_function_SetSavePath)
        button_set_save_path.grid(row=4, column=0, columnspan=2, sticky="e")

        # Label, um den aktuellen Speicherpfad anzuzeigen
        save_path_label = Label(user_frame_1, text="Save Path: Not Set")
        save_path_label.grid(row=5, column=0, columnspan=2, sticky="w")

        # Buttons für DB-Operationen
        button_width = 20  # Breite der Buttons
        button_height = 4  # Höhe der Buttons

        Button(user_frame_1, text="Save DB Config", width=button_width, height=button_height,
               command=lambda: button_function_WrDB(entry_host.get(), entry_user.get(), entry_db.get())).grid(row=6, column=0, columnspan=2, sticky="e")

        Button(user_frame_1, text="Save DB ALL", width=button_width, height=button_height,
               command=button_function_Save_all).grid(row=7, column=0, columnspan=2, sticky="e")

        Button(user_frame_1, text="Save DB Day", width=button_width, height=button_height,
               command=lambda: button_function_Save_Day(entry_Date.get())).grid(row=8, column=0, columnspan=2, sticky="e")

        for widget in user_frame_1.winfo_children():
            widget.grid_configure(padx=20, pady=5)

        return save_path_label

    except Exception as e:
        print(f"Fehler beim Erstellen der GUI: {e}")

def open_database_settings(Main_GUI):
    db_settings_window = Toplevel(Main_GUI)
    db_settings_window.title("Database Settings")
