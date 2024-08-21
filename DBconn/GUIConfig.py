import tkinter as tk
import winreg
from tkinter import ttk, Entry, Label, Button, Toplevel
from tkinter.filedialog import askdirectory
from tkcalendar import DateEntry
from DBConfig import Read_Config, Write_Config

def HomeScreenConfig(Main_GUI, host, user, database, save_path_all, save_path_day,
                     button_function_WrDB, button_function_Save_all, button_function_Save_Day):
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

        Label(user_frame_1, text="Host").grid(row=1, column=0)
        entry_host.grid(row=1, column=1)
        entry_host.insert(0, host)

        Label(user_frame_1, text="User").grid(row=2, column=0)
        entry_user.grid(row=2, column=1)
        entry_user.insert(0, user)

        Label(user_frame_1, text="Database").grid(row=3, column=0)
        entry_db.grid(row=3, column=1)
        entry_db.insert(0, database)

        # Speicherpfadeingaben
        Label(user_frame_1, text="Save Path All").grid(row=4, column=0)
        entry_save_path_all = ttk.Entry(user_frame_1, width=23, justify="right")
        entry_save_path_all.grid(row=4, column=1)
        entry_save_path_all.insert(0, save_path_all)
        entry_save_path_all.config(state=tk.DISABLED)

        Label(user_frame_1, text="Save Path Day").grid(row=5, column=0)
        entry_save_path_day = ttk.Entry(user_frame_1, width=23, justify="right")
        entry_save_path_day.grid(row=5, column=1)
        entry_save_path_day.insert(0, save_path_day)
        entry_save_path_day.config(state=tk.DISABLED)

        # Buttons
        button_width = 20  # Ändere die Breite nach Bedarf
        button_height = 4

        Button(user_frame_1, text="Save DB Config", width=button_width, height=button_height,
               command=lambda: button_function_WrDB(entry_host.get(), entry_user.get(), entry_db.get())).grid(row=6, column=0, columnspan=2, sticky="e")

        Button(user_frame_1, text="Save DB ALL", width=button_width, height=button_height,
               command=button_function_Save_all).grid(row=7, column=0, columnspan=2, sticky="e")

        Button(user_frame_1, text="Save DB Day", width=button_width, height=button_height,
               command=lambda: button_function_Save_Day(entry_Date.get())).grid(row=8, column=0, columnspan=2, sticky="e")

        Button(user_frame_1, text="Select Save Path All", width=button_width, height=button_height,
               command=lambda: set_save_path_and_update_config(Main_GUI, entry_save_path_all, 't_save_path_all')).grid(row=9, column=0, columnspan=2, sticky="e")

        Button(user_frame_1, text="Select Save Path Day", width=button_width, height=button_height,
               command=lambda: set_save_path_and_update_config(Main_GUI, entry_save_path_day, 't_save_path_day')).grid(row=10, column=0, columnspan=2, sticky="e")

        for widget in user_frame_1.winfo_children():
            widget.grid_configure(padx=20, pady=5)
    except Exception as e:
        print(f"Fehler beim Erstellen der GUI: {e}")


def set_save_path_and_update_config(root, entry_widget, config_key):
    selected_path = askdirectory(parent=root)
    if selected_path:
        entry_widget.config(state=tk.NORMAL)
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, selected_path)
        entry_widget.config(state=tk.DISABLED)

        # Update the config.ini with the new path
        config = Read_Config()
        if config_key == 't_save_path_all':
            Write_Config(config['t_host'], config['t_user'], config['t_database'], selected_path, config['t_save_path_day'])
        elif config_key == 't_save_path_day':
            Write_Config(config['t_host'], config['t_user'], config['t_database'], config['t_save_path_all'], selected_path)
