import sqlite3
import tkinter as tk
import datetime


# В этом классе проводятся операции с базой данных

class DataBase:
    def __init__(self):
        super().__init__()

        # Создание БД
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS database (
                ids INT,
                day INT,
                task TEXT
            )
        """)

        # Проверка на необходимость изменения бд
        self.CheckingForTheNeedToChangeTheDatabase()

    def CheckingForTheNeedToChangeTheDatabase(self):
        # Если бд пустая создать строчку -1 -1 *текущая дата*
        self.c.execute('SELECT COUNT(*) FROM database')
        result = self.c.fetchone()

        if result[0] == 0:
            print('База данных пустая')
            self.c.execute("INSERT INTO database (ids, day, task) VALUES (?, ?, ?)",
                           (-1, -1, datetime.date.today()))

        # Если сегодняшняя дата не совпадает с датой в первой строчке, то мы меняем первую строчку
        # и удаляем лишние (уже неактуальные) задачи

        self.c.execute('SELECT task FROM database LIMIT 1')
        result = self.c.fetchone()  # Получение первой строки
        value_from_db = result[0]

        # Если число в первой строке не совпадает с сегодняшним, удаляем неакт. задания и обновляем первую строку
        if str(datetime.date.today()) != value_from_db:
            self.c.execute("DELETE FROM database WHERE day < ?", (datetime.date.today(),))
            self.c.execute("UPDATE database SET task = ? WHERE ids = -1", (datetime.date.today(),))

            if str(datetime.date.today().month) != value_from_db.month or str(
                    datetime.date.today().year) != value_from_db.year:
                self.c.execute("DROP TABLE IF EXISTS database")
                self.c.execute("INSERT INTO database (ids, day, task) VALUES (?, ?, ?)",
                               (-1, -1, datetime.date.today()))

        self.conn.commit()
    def DeleteTaskFromDB(self, window, ids, date, task):
        self.c.execute("DELETE FROM database WHERE day = ? AND task = ? AND ids = ?;", (date.day, task, ids))
        self.c.execute("UPDATE database SET ids = ids - 1 WHERE day = ? AND ids > ?;", (date.day, ids))
        self.conn.commit()

        # Удаление всех дочерних виджетов.
        # В нашем случае удаление всех дел для того чтобы потом загрузить обновленный список
        for widget in window.winfo_children():
            widget.destroy()

        DataBase.PutAllFromDB(self, window, date)

    def CountTasksInDBWithSameDay(self, day):
        # Используется для создания корректного id, который будет равен количеству уже существующих строк
        self.c.execute("SELECT COUNT(*) FROM database WHERE day = ?", (day.day,))
        return self.c.fetchone()[0]

    def PutAllFromDB(self, window, date):
        self.c.execute("SELECT * FROM database WHERE day = ?", (date.day,))

        # Получение результатов в виде массива
        self.results = self.c.fetchall()

        # Для того чтобы чекбоксы были пусты
        checkbox_state = tk.BooleanVar()
        checkbox_state.set(False)

        # Вывод элементов
        for row in self.results:
            res = tk.Checkbutton(window,
                                 font=("Trebuchet MS bold", 12),
                                 background='#bfbfbf',
                                 text=row[2],
                                 variable=checkbox_state,
                                 anchor='w',
                                 command=lambda ids=row[0], day=row[1], task=row[2]: DataBase.DeleteTaskFromDB(self,
                                                                                                               window,
                                                                                                               ids,
                                                                                                               date,
                                                                                                               task))
            res.place(relx=0, rely=0.125 * row[0], relwidth=1, relheight=0.1)

    def AddTaskToDB(self, window, date, task, entry):
        self.c.execute("INSERT INTO database (ids, day, task) VALUES (?, ?, ?)",
                       (DataBase.CountTasksInDBWithSameDay(self, date), date.day, task))
        self.conn.commit()
        entry.delete(0, tk.END)
        DataBase.PutAllFromDB(self, window, date)
