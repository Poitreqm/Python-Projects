import tkinter as tk
from tkinter import ttk
from datetime import datetime
import time

root = tk.Tk()
root.title("Time - Calc - Alarm - Calendar - Timer - Stopwatch")
root.geometry("600x600")

# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=tk.BOTH)


def current_day_of_week():
    get_day = datetime.weekday(
        datetime.now()
    )  # получаем текущий день где 0 - понедельник, а 6 воскресенье

    if get_day == 0:
        return "Monday"
    elif get_day == 1:
        return "Tuesday"
    elif get_day == 2:
        return "Wednesday"
    elif get_day == 3:
        return "Thursday"
    elif get_day == 4:
        return "Friday"
    elif get_day == 5:
        return "Saturday"
    elif get_day == 6:
        return "Sunday"


def update_time():
    current_time = time.strftime("%H:%M:%S")
    current_day = datetime.date(datetime.now())
    current_day_of_week_now = current_day_of_week()

    time_now = ttk.Label(frame_time, text=f"{current_time}")
    data_now = ttk.Label(frame_time, text=f"{current_day}")
    current_day_of_week_now = ttk.Label(frame_time, text=f"{current_day_of_week_now}")

    time_now.place(rely=0.02, relx=0.5, anchor="center")  # отображение времени
    data_now.place(rely=0.05, relx=0.5, anchor="center")  # отображение даты
    current_day_of_week_now.place(rely=0.08, relx=0.5, anchor="center")

    time_now.config(text=current_time)
    root.after(
        1000, update_time
    )  # обновляет каждые 1 секунду время. Это нужно что бы шел счетчик секунд и время всегда было актуальным.


# expand=True указывает, что виджет должен растягиваться по горизонтали и вертикали в соответствии с размерами своего родительского контейнера.
# fill=BOTH указывает, что виджет должен заполнить пространство, выделенное для него, как по горизонтали, так и по вертикали.

print()

# создаем пару фреймвов
frame_time = ttk.Frame(notebook)
frame_calculator = ttk.Frame(notebook)
frame_alarm = ttk.Frame(notebook)
frame_calendar = ttk.Frame(notebook)
frame_timer = ttk.Frame(notebook)
frame_stopwatch = ttk.Frame(notebook)

frame_time.pack(expand=True, fill=tk.BOTH)
frame_calculator.pack(expand=True, fill=tk.BOTH)

update_time()


# добавляем фреймы в качестве вкладок
notebook.add(frame_time, text="Time")
notebook.add(frame_calculator, text="Calculator")
notebook.add(frame_alarm, text="Alarm")
notebook.add(frame_calendar, text="Calendar")
notebook.add(frame_timer, text="Timer")
notebook.add(frame_stopwatch, text="Stopwatch")

current_day_of_week()

root.mainloop()
