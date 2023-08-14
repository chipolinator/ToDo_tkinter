import getpass
import threading
import tkinter as tk
import datetime
import calendar
import time
import pygame

from functools import partial
from tkinter import *
from tkinter.messagebox import showinfo
from model import DataBase


# В данном классе создаются все элементы представления

class View:
    class Header(tk.Frame):
        # Хэдер с иконкой и приветствием пользователя
        def __init__(self, parent):
            super().__init__(parent)

            self['background'] = self.master['background']

            self.put_widgets()

        def put_widgets(self):
            global ico1
            ico1 = tk.PhotoImage(file="icons/ico1.png")

            # Приветствие
            Label(self,
                  text="    Good evening, " + getpass.getuser(),
                  background=self.master['background'],
                  font=("Trebuchet MS bold", 24),
                  anchor='w').place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

            # Иконка
            Label(self,
                  background=self.master['background'],
                  image=ico1).place(relx=0, rely=0, relwidth=0.2, relheight=1)

    class AddTasks(tk.Frame):
        # + Entry clock - инструменты для ввода новых задач
        def __init__(self, parent, TodaysDate):
            super().__init__(parent)

            self['background'] = self.master['background']

            self.put_widgets(TodaysDate)

        def put_widgets(self, TodaysDate):
            global ico4, ico5
            ico4 = tk.PhotoImage(file="icons/ico4.png")
            ico5 = tk.PhotoImage(file="icons/ico5.png")

            # создаем рамку для задач
            self.tasks_frame = tk.Frame(self, bg='#f7f7f7')
            self.tasks_frame.place(relx=0, rely=0, relwidth=1, relheight=0.85)

            # выводим все задачи из бд
            self.model = DataBase()
            self.model.PutAllFromDB(self.tasks_frame, TodaysDate)

            # поле ввода
            self.entry = tk.Entry(self)
            self.entry.place(relx=0.075, rely=0.9, relwidth=0.85, relheight=0.075)

            # +
            tk.Button(self, relief=tk.FLAT, image=ico4, background=self.master['background'],
                      command=lambda: self.model.AddTaskToDB(self.tasks_frame, TodaysDate, self.entry.get(),
                      self.entry)).place(relx=0, rely=0.9, relwidth=0.075, relheight=0.075)

            # кнопка таймера
            tk.Button(self, relief=tk.FLAT, image=ico5, background=self.master['background'],
                      command=lambda: self.MakeAClockWindow(TodaysDate,
                      self.entry.get())).place(relx=0.925, rely=0.9, relwidth=0.075, relheight=0.075)

        def MakeAClockWindow(self, TodaysDate, text):
            def count_down(hours, minits, text):
                # Уничтожение доп окна
                clockWindow.destroy()

                # Отсчет необходимого времени
                WaitTime = 60 * minits + 60 * 60 * hours
                for i in range(1, int(WaitTime) + 1):
                    time.sleep(1)

                # Запуск зввука
                pygame.mixer.init()
                pygame.mixer.music.load('music.mp3')
                pygame.mixer.music.play()

                # Вызов уведомления
                showinfo("Timer", text)

            def start_timer():
                # Добавляем задачу в список
                self.model.AddTaskToDB(self.tasks_frame, TodaysDate, self.entry.get(), self.entry)

                # Берем переданные пользователем данные и начинаем поток
                hours = hour1.get()
                if hours == '':
                    hours = 0
                else:
                    hours = int(hours)
                minits = int(min1.get())

                t = threading.Thread(target=count_down, args=(hours, minits, text))
                t.start()

            # Создание окна для таймера
            clockWindow = tk.Toplevel(self)
            clockWindow.geometry("500x300")
            clockWindow.resizable(width=False, height=False)
            clockWindow.iconbitmap('icons/1.ico')

            # Основная рамка
            clockFrame = tk.Frame(clockWindow, background='white')
            clockFrame.place(relx=0, rely=0, relwidth=1, relheight=0.7)

            # Поле для ввода часов
            hour1 = tk.Entry(clockFrame, font=("Trebuchet MS bold", 50), bg='white')
            hour1.place(relx=0.1, rely=0.2, relwidth=0.19, relheight=0.45)

            # Текстовое поле
            hour2 = tk.Label(clockFrame, text="час. ", anchor='s', font=("Trebuchet MS bold", 24), bg='white')
            hour2.place(relx=0.3, rely=0.2, relwidth=0.2, relheight=0.5)

            # Поле для ввода минут
            min1 = tk.Entry(clockFrame, font=("Trebuchet MS bold", 50), bg='white')
            min1.place(relx=0.5, rely=0.2, relwidth=0.19, relheight=0.45)

            # Текстовое поле
            min2 = tk.Label(clockFrame, text="мин. ", anchor='s', font=("Trebuchet MS bold", 24), bg='white')
            min2.place(relx=0.7, rely=0.2, relwidth=0.2, relheight=0.5)

            # Кнопка которая запускает таймер
            enterClock = tk.Button(clockWindow,
                                   relief=tk.FLAT,
                                   text='Set a reminder',
                                   font=("Trebuchet MS bold", 24),
                                   background='#122faa',
                                   command=start_timer)
            enterClock.place(relx=0, rely=0.7, relwidth=1, relheight=0.3)

    class MainFrame2(tk.Frame):
        # вывод дней на которые можно записать задачи, переход по кнопке Next 5 days
        def __init__(self, parent):
            super().__init__(parent)

            self['background'] = self.master['background']

            self.put_widgets()

        def put_widgets(self):
            # Вывод пяти кнопок на экран
            for i in range(5):
                date = datetime.date.today() + datetime.timedelta(days=i + 1)

                button = tk.Button(self, bd=1, relief="groove", font=("Trebuchet MS bold", 28), background='white',
                                   text=date.strftime("%e"),
                                   command=lambda date=date: self.master.put_main_frames(const=0, TodaysDate=date))
                button.place(relx=0.208 * i + 0.01, rely=0.02, relwidth=0.15, relheight=0.2)

    class MainFrame1(tk.Frame):
        # дефолтный экран, экран при переходе на кнопку today
        def __init__(self, parent, TodaysDate):
            super().__init__(parent)

            self.TodaysDate = TodaysDate
            self['background'] = self.master['background']

            self.put_widgets()

        def put_widgets(self):
            # вывод числа, дня недели и месяца на главный экран
            self.day_name = self.TodaysDate.day
            self.month_name = calendar.month_name[self.TodaysDate.month]
            self.weekday_name = calendar.day_name[self.TodaysDate.weekday()]

            # День недели
            self.WeekDayLabel = tk.Label(self, text=self.weekday_name, font=("Trebuchet MS bold", 12),
                                         background=self.master['background'])
            self.WeekDayLabel.place(relx=0.01, rely=0.02, relwidth=0.15, relheight=0.04)

            # Число
            self.DayLabel = tk.Label(self, text=self.day_name, font=("Trebuchet MS bold", 28),
                                     background=self.master['background'])
            self.DayLabel.place(relx=0.01, rely=0.06, relwidth=0.15, relheight=0.12)

            # Месяц
            self.MonthLabel = tk.Label(self, text=self.month_name, font=("Trebuchet MS bold", 12),
                                       background=self.master['background'])
            self.MonthLabel.place(relx=0.01, rely=0.17, relwidth=0.15, relheight=0.04)

            # Вывод на экран основной рабочей поверхности для заданий
            self.add_tasks_frame = View.AddTasks(self, self.TodaysDate)
            self.add_tasks_frame.place(relx=0.2, rely=0.02, relwidth=0.75, relheight=0.925)

    class Buttons(tk.Frame):
        # кнопки в столбце слева
        def __init__(self, parent):
            super().__init__(parent)

            self['background'] = self.master['background']

            self.put_widgets()

        def put_widgets(self):
            global ico2, ico3

            ico2 = tk.PhotoImage(file="icons/ico2.png")
            ico3 = tk.PhotoImage(file="icons/ico3.png")

            # Кнопка Today и иконка
            self.TodayLabelIcon = tk.Label(self, image=ico2, background=self.master['background'])
            self.TodayLabelIcon.place(relx=0.05, rely=0.01, relwidth=0.2, relheight=0.075)

            self.TodayLabel = tk.Button(self, relief=tk.FLAT, text="Today", background=self.master['background'],
                                        command=partial(self.master.put_main_frames, 0))
            self.TodayLabel.place(relx=0.25, rely=0.01, relwidth=0.75, relheight=0.075)


            # Кнопка Next 5 days и иконка
            self.Next5DaysLabelIco = tk.Label(self, image=ico3, background=self.master['background'])
            self.Next5DaysLabelIco.place(relx=0.05, rely=0.076, relwidth=0.2, relheight=0.075)

            self.Next5DaysLabel = tk.Button(self, relief=tk.FLAT, text="Next 5 days",
                                            background=self.master['background'],
                                            command=partial(self.master.put_main_frames, 1))
            self.Next5DaysLabel.place(relx=0.25, rely=0.076, relwidth=0.75, relheight=0.075)
