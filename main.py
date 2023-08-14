import datetime
import tkinter as tk
from tkinter import ttk

from view import View

# В данном классе запускается окно приложения вместе с основными элементами в нем

class NevaApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Создание окна
        self.title("Neva")
        self.resizable(width=False, height=False)
        self.iconbitmap('icons/1.ico')
        self.geometry("1000x700")

        # Родительские параметры
        self['background'] = 'white'
        self.bold_font = ("Trebuchet MS bold", 12)

        # Функции
        self.put_main_frames()

    # TodaysDate это сегодняшняя дата в формате гггг-мм-дд
    def put_main_frames(self, const=0, TodaysDate=datetime.date.today()):
        self.header_frame = View.Header(self)
        self.header_frame.place(relwidth=1, relheight=0.2)

        self.buttons_frame = View.Buttons(self)
        self.buttons_frame.place(relx=0, rely=0.2, relwidth=0.2, relheight=0.8)

        # если const==0 то на экран выводится "основное" окно, иначе же выводится окно с пятью кнопками
        if const == 0:
            self.TodaysDate = TodaysDate
            self.main_frame1 = View.MainFrame1(self, self.TodaysDate)
            self.main_frame1.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)
        elif const == 1:
            self.main_frame2 = View.MainFrame2(self)
            self.main_frame2.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)

        ttk.Separator(self, orient='horizontal').place(relx=0, rely=0.2, relwidth=1, relheight=0.0000001)
        ttk.Separator(self, orient='vertical').place(relx=0.2, rely=0, relwidth=0.0000001, relheight=1)


if __name__ == '__main__':
    app = NevaApp()
    app.mainloop()
