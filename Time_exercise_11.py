#
# Программа которая показывает текущее время в режиме онлайн, дату и день недели
#

import tkinter as tk
from tkinter import ttk
from datetime import datetime
import time

root = tk.Tk()
root.title("Current time")
root.geometry("300x300")

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

    time_now = ttk.Label(frame_time, text=f"{current_time}", font="Courier 20")
    data_now = ttk.Label(frame_time, text=f"{current_day}", font="Courier 20")
    current_day_of_week_now = ttk.Label(
        frame_time, text=f"{current_day_of_week_now}", font="Courier 20"
    )

    time_now.place(rely=0.2, relx=0.5, anchor="center")  # отображение времени
    data_now.place(rely=0.32, relx=0.5, anchor="center")  # отображение даты
    current_day_of_week_now.place(rely=0.44, relx=0.5, anchor="center")

    time_now.config(text=current_time)
    root.after(
        1000, update_time
    )  # обновляет каждые 1 секунду время. Это нужно что бы шел счетчик секунд и время всегда было актуальным.


# expand=True указывает, что виджет должен растягиваться по горизонтали и вертикали в соответствии с размерами своего родительского контейнера.
# fill=BOTH указывает, что виджет должен заполнить пространство, выделенное для него, как по горизонтали, так и по вертикали.

frame_time = ttk.Frame(notebook)
frame_time.pack(expand=True, fill=tk.BOTH)

update_time()
current_day_of_week()

root.mainloop()
