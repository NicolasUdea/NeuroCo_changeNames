import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os
import glob

def rename_files():
    start_time = start_entry.get()
    end_time = end_entry.get()
    new_name = name_entry.get()

    if not start_time or not end_time or not new_name:
        messagebox.showerror("Error", "Por favor, rellena todos los campos.")
        return

    csv_files = glob.glob('*.csv')
    for file in csv_files:
        df = pd.read_csv(file)
        time_col = pd.to_datetime(df['time'])  # Asumir que 'time' es el nombre de la columna de tiempo
        mask = (time_col >= start_time) & (time_col <= end_time)
        if df.loc[mask].shape[0] > 0:
            os.rename(file, new_name + '.csv')

root = tk.Tk()

start_label = tk.Label(root, text="Hora de inicio (formato HH:MM:SS):")
start_label.pack()
start_entry = tk.Entry(root)
start_entry.pack()

end_label = tk.Label(root, text="Hora de fin (formato HH:MM:SS):")
end_label.pack()
end_entry = tk.Entry(root)
end_entry.pack()

name_label = tk.Label(root, text="Nuevo nombre:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

button = tk.Button(root, text="Cambiar nombres", command=rename_files)
button.pack()

root.mainloop()
