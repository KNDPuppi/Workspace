
import tkinter as tk
from tkinter import ttk
import configparser
from datetime import datetime, timedelta
import threading
import time
import DBConfig
import GUIConfig

def save_all():
    # Funktion zum Speichern aller Daten
    pass

def save_day(date):
    # Funktion zum Speichern von Tagesdaten
    pass

def schedule_daily_task(scheduled_time):
    now = datetime.now()
    scheduled_time = datetime.strptime(scheduled_time, "%H:%M").time()
    first_run_time = datetime.combine(now.date(), scheduled_time)

    if now.time() > scheduled_time:
        first_run_time += timedelta(days=1)

    delay = (first_run_time - now).total_seconds()
    threading.Timer(delay, run_daily_task, [scheduled_time]).start()

def run_daily_task(scheduled_time):
    now = datetime.now()
    scheduled_time = datetime.strptime(scheduled_time, "%H:%M").time()
    if now.time() >= scheduled_time:
        # Hier die Funktion aufrufen, die ausgeführt werden soll
        DBConfig.DBSaveCurDay(host, user, database, now.strftime('%Y-%m-%d'), save_path_day)
        schedule_daily_task(scheduled_time)

def read_config():
    config = DBConfig.Read_Config()
    global host, user, database, save_path_all, save_path_day, scheduled_time
    host = config['t_host']
    user = config['t_user']
    database = config['t_database']
    save_path_all = config['save_path_all']
    save_path_day = config['save_path_day']
    scheduled_time = config['scheduled_time']

def on_save_config():
    # Konfigurationsspeicherfunktion
    DBConfig.Write_Config(entry_host.get(), entry_user.get(), entry_db.get(), entry_time.get())
    read_config()
    schedule_daily_task(entry_time.get())

def main():
    global entry_host, entry_user, entry_db, entry_time
    root = tk.Tk()

    # Setze die GUI basierend auf den Konfigurationen
    save_path_all_var = tk.StringVar(value="...")
    save_path_day_var = tk.StringVar(value="...")
    time_entry_var = tk.StringVar(value="00:00")

    read_config()
    GUIConfig.HomeScreenConfig(root, host, user, database, save_all, save_day, lambda date: DBConfig.DBSaveCurDay(host, user, database, date, save_path_day), save_path_all_var, save_path_day_var, time_entry_var)

    root.mainloop()

if __name__ == "__main__":
    main()