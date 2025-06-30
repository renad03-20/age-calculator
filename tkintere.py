import tkinter as tk
import ttkbootstrap as ttk
from datetime import datetime
from dateutil.relativedelta import relativedelta

def convert():
    years = entry_int_years.get()
    months = entry_int_months.get()
    days = entry_int_days.get()

    birthdate = datetime(years, months, days)

    now = datetime.now()

    age = relativedelta(now, birthdate)

    delta = now - birthdate
    total_seconds = int(delta.total_seconds())
    total_minutes = total_seconds // 60
    total_hours = total_minutes // 60
    output_string_years.set(f'{age.years} years')
    output_string_months.set(f'{age.months} months')
    output_string_dyas.set(f'{age.days} days')
    output_string_hours.set(f'{total_hours} hours')
    output_string_minutes.set(f'{total_minutes} minutes')
    output_string_seconds.set(f'{total_seconds} seconds')

root = ttk.Window(themename='darkly')
root.title("Demo")
root.geometry('650x650')

name = ttk.Label(master= root, text='calculate your age in years months weeks hours minutes seconds in one click ', font='Calibri 13 bold')
name.pack()

input_frame = ttk.Frame(master=root)

entry_int_years = tk.IntVar()
entry_int_months = tk.IntVar()
entry_int_days = tk.IntVar()

entry_years = ttk.Entry(master = input_frame, textvariable = entry_int_years)
entry_months = ttk.Entry(master = input_frame, textvariable = entry_int_months)
entry_days = ttk.Entry(master = input_frame, textvariable = entry_int_days)

button = ttk.Button(master = input_frame, text='calculate', command = convert)

entry_years.pack(pady= 10)
entry_months.pack(pady= 10)
entry_days.pack(pady= 10)

button.pack(pady= 10)

input_frame.pack(pady= 10)


output_string_years = tk.StringVar()
output_string_months = tk.StringVar()
output_string_dyas = tk.StringVar()
output_string_hours = tk.StringVar()
output_string_minutes = tk.StringVar()
output_string_seconds = tk.StringVar()

output_label_years = ttk.Label(master=root, text="output",font='Calibri 24', textvariable = output_string_years)
output_label_months = ttk.Label(master=root, text="output",font='Calibri 24', textvariable = output_string_months)
output_label_dyas = ttk.Label(master=root, text="output",font='Calibri 24', textvariable = output_string_dyas)
output_label_hours = ttk.Label(master=root, text="output",font='Calibri 24', textvariable = output_string_hours)
output_label_minutes = ttk.Label(master=root, text="output",font='Calibri 24', textvariable = output_string_minutes)
output_label_seconds = ttk.Label(master=root, text="output",font='Calibri 24', textvariable = output_string_seconds)

output_label_years.pack(pady= 10)
output_label_months.pack(pady= 10)
output_label_dyas.pack(pady= 10)
output_label_hours.pack(pady= 10)
output_label_minutes.pack(pady= 10)
output_label_seconds.pack(pady= 10)


root.mainloop()