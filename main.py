import getpass
import tkinter as tk
import datetime
import calendar
from functools import partial
from tkinter import *
from tkinter import ttk

class NevaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # Создание окна
        self.title("Neva")
        self.resizable(width=False, height=False)
        self.iconbitmap('1.ico')
        self.geometry("1000x700")

        # Родительские параметры
        self['background'] = 'white'
        self.bold_font = ("Trebuchet MS bold", 12)

        # Функции
        self.put_main_frames()

        # Сепараторы
        ttk.Separator(self, orient='horizontal').place(relx=0, rely=0.2, relwidth=1, relheight=0.0000001)
        ttk.Separator(self, orient='vertical').place(relx=0.2, rely=0, relwidth=0.0000001, relheight=1)

    def put_main_frames(self, const=0):

        self.header_frame = Header(self)
        self.header_frame.place(relwidth=1, relheight=0.2)
        self.buttons_frame = Buttons(self)
        self.buttons_frame.place(relx=0, rely=0.2, relwidth=0.2, relheight=0.8)

        if const == 0:
            self.main_frame = MainFrame1(self)
            self.main_frame.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)
        elif const == 1:
            self.main_frame = MainFrame2(self)
            self.main_frame.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)

        ttk.Separator(self, orient='horizontal').place(relx=0, rely=0.2, relwidth=1, relheight=0.0000001)
        ttk.Separator(self, orient='vertical').place(relx=0.2, rely=0, relwidth=0.0000001, relheight=1)






class Header(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']

        self.put_widgets()

    def put_widgets(self):
        global ico1
        Label(self,
              text="    Good evening, " + getpass.getuser(),
              background=self.master['background'],
              font=("Trebuchet MS bold", 24),
              anchor='w').place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

        ico1 = PhotoImage(file="ico1.png")
        Label(self,
              background=self.master['background'],
              image=ico1).place(relx=0, rely=0, relwidth=0.2, relheight=1)





class MainFrame2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        for i in range(5):
            date = datetime.date.today() + datetime.timedelta(days=i+1)
            button = tk.Button(self, bd=1, relief="groove", font=("Trebuchet MS bold", 28), background='white',
                               text=date.strftime("%d"))
            button.place(relx=0.208 * i + 0.01, rely=0.02, relwidth=0.15, relheight=0.2)



class MainFrame1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        # Вывод числа, месяца и дня недели
        self.date_frame = DATE(self)
        self.date_frame.place(relx=0.01, rely=0.02, relwidth=0.15, relheight=0.2)
        self.tasks_frame = Tasks(self)
        self.tasks_frame.place(relx=0.2, rely=0.02, relwidth=0.75, relheight=0.85)
        self.add_tasks_frame = Add(self)
        self.add_tasks_frame.place(relx=0.2, rely=0.9, relwidth=0.75, relheight=0.075)


class Add(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()
    def put_widgets(self):
        global ico4, ico5
        ico4 = tk.PhotoImage(file="ico4.png")
        # +
        Button(self,
               relief=FLAT,
               image=ico4,
               background=self.master['background']).place(relx=0, rely=0, relwidth=0.075, relheight=1)
        # поле ввода
        Entry(self).place(relx=0.075, rely=0, relwidth=0.85, relheight=1)
        # кнопка таймера
        ico5 = PhotoImage(file="ico5.png")
        Button(self,
               relief=FLAT,
               image=ico5,
               background=self.master['background']).place(relx=0.925, rely=0, relwidth=0.075, relheight=1)

class DATE(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        today = datetime.date.today()  # Получение текущей даты
        day_name = today.day
        month_name = calendar.month_name[today.month]
        weekday_name = calendar.day_name[today.weekday()]

        # вывод недели/дня/месяца
        Label(self,
              text=weekday_name,
              font=("Trebuchet MS bold", 12),
              background=self.master['background']).place(relx=0, rely=0, relwidth=1, relheight=0.2)
        Label(self,
              text=day_name,
              font=("Trebuchet MS bold", 28),
              background=self.master['background']).place(relx=0, rely=0.2, relwidth=1, relheight=0.6)
        Label(self,
              text=month_name,
              font=("Trebuchet MS bold", 12),
              background=self.master['background']).place(relx=0, rely=0.8, relwidth=1, relheight=0.2)

class Tasks(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = '#f7f7f7'
        #self.put_widgets()

    #def put_widgets(self):
        # тут будут появляться задачи

class Buttons(tk.Frame, NevaApp):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()


    def put_widgets(self):
        global ico2, ico3
        # объявляем иконки глобальными переменными иначе они не будут отображаться

        # первая кнопка с иконкой переносящая на главный экран
        ico2 = PhotoImage(file="ico2.png")
        Label(self,
              image=ico2,
              background=self.master['background']).place(relx=0.05, rely=0.01, relwidth=0.2, relheight=0.075)

        Button(self,
               relief=FLAT,
               text="Today",
               background=self.master['background'],
               command=partial(self.master.put_main_frames, 0)).place(relx=0.25, rely=0.01, relwidth=0.75, relheight=0.075)

        # вторая кнопка с иконкой переносящая на клалендарик
        ico3 = PhotoImage(file="ico3.png")
        Label(self,
              image=ico3,
              background=self.master['background']).place(relx=0.05, rely=0.076, relwidth=0.2, relheight=0.075)

        Button(self,
               relief=FLAT,
               text="Next 5 days",
               background=self.master['background'],
               command=partial(self.master.put_main_frames, 1)).place(relx=0.25, rely=0.076, relwidth=0.75, relheight=0.075)


app = NevaApp()
app.mainloop()
