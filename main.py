from tkinter import *
from tkinter import ttk
from datetime import datetime
import datetime
from tkinter import font
import threading
import time
import tkinter as tk
from playsound import playsound
from tkinter.messagebox import showinfo
import sqlite3
import os


lblist = []

conn = sqlite3.connect('database.db')
c = conn.cursor()

conn.execute("""
                CREATE TABLE IF NOT EXISTS  database (
                    day INT,
                    task TEXT
                );
            """)
conn.commit()


window = Tk()
window.title("Neva")
window.resizable(width=False, height=False)
window.iconbitmap('1.ico')
window.geometry("1000x700")

today = datetime.date.today()
weekday = today.weekday()
the_day = today.day
month = today.month
textADD = the_day

dick1 = {'6':'Sunday','0':'Monday','1':'Tuesday','2':'Wednesday','3':'Thursday','4':'Friday','5':'Saturday'}
dick2 = {'1':'January','2':'February','3':'March', '4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}

enabled = IntVar()

frameWEEK = tk.Frame(window, background="white", bd=1, relief="groove")
frameWEEK.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)

def buttonClickWEEK(text):
    global textADD
    textADD = text
    dateDAY2.config(text=text)
    global lblist
    lblist = []
    my_list = []
    i = str(int(textADD) - the_day + 1)

    # Удаление всех дочерних виджетов на things
    for widget in things.winfo_children():
        widget.destroy()

    c.execute("SELECT * FROM database WHERE day = " + i)
    print(i)
    rows = c.fetchall()
    print(rows)
    for row in rows:
        my_list.append(row[1])
        enabled = IntVar()
        i = len(lblist)
        res = tk.Checkbutton(things,
                             font=("Trebuchet MS bold", 12),
                             background='white',
                             text=row[1],
                             variable=enabled,
                             anchor='w',
                             command=lambda i=i: on_checked(lblist[i]))

        res.place(relx=0, rely=0.125 * (len(my_list)-1), relwidth=1, relheight=0.1)
        lblist.append(res)
    main.tkraise()





buttons = []
for i in range(1, 6):
    date = today + datetime.timedelta(days=i)
    button = tk.Button(frameWEEK, bd=1, relief="groove", font=("Trebuchet MS bold", 28),
                 background='white', text=date.strftime("%d"), command=lambda text=date.strftime("%d"): buttonClickWEEK(text))
    buttons.append(button)

for i, button in enumerate(buttons):
    button.place(relx=0.208*(i)+0.01, rely=0.02, relwidth=0.15, relheight=0.2)

def on_checked(ch):
    if ch["bg"] == "white":
        ch["font"] = font.Font(family="Trebuchet MS ", size=12, overstrike=True)
        ch.config(bg="gray")

    else:
        ch['font'] = font.Font(family= "Trebuchet MS ", size=12, overstrike=False)
        ch.config(bg="white")

def addlabel():
    enabled = IntVar()
    i = len(lblist)
    res = tk.Checkbutton(things,
                         font=("Trebuchet MS bold", 12),
                         background='white',
                         text=add2.get(),
                         variable=enabled,
                         anchor='w',
                         command=lambda i=i: on_checked(lblist[i]))
    c.execute("INSERT INTO database VALUES(?, ?);", (int(textADD)-the_day+1, add2.get()))
    conn.commit()
    res.place(relx=0, rely=0.125*(len(lblist)), relwidth=1, relheight=0.1)
    lblist.append(res)
    add2.delete(0, END)


def timer1():
    def count_down(a,b,c):
        timeer = 60*b+60*60*a
        newWindow.destroy()
        for i in range(1,int(timeer)+1):
            time.sleep(1)
        playsound('music.mp3')
        showinfo("Timer", c)

    def start_timer():
        a = hour1.get()
        if a == '':
            a = 0
        else:
            a = int(a)
        b = int(min1.get())
        c = add2.get()
        # Создаем поток
        addlabel()
        t = threading.Thread(target=count_down, args=(a,b,c))
        t.start()
        # Запускаем поток

    newWindow = tk.Toplevel(window)
    newWindow.geometry("500x300")
    newWindow.resizable(width=False, height=False)
    newWindow.iconbitmap('1.ico')

    clockFrame = Frame(newWindow, background='white')
    clockFrame.place(relx=0, rely=0, relwidth=1, relheight=0.7)

    hour1 = Entry(clockFrame,font=("Trebuchet MS bold", 50),bg='white')
    hour1.place(relx=0.1, rely=0.2, relwidth=0.19, relheight=0.45)
    hour2 = Label(clockFrame,text="час. ", anchor='s', font=("Trebuchet MS bold", 24),bg='white')
    hour2.place(relx=0.3, rely=0.2, relwidth=0.2, relheight=0.5)
    min1 = Entry(clockFrame,font=("Trebuchet MS bold", 50),bg='white')
    min1.place(relx=0.5, rely=0.2, relwidth=0.19, relheight=0.45)
    min2 = Label(clockFrame,text="мин. ", anchor='s', font=("Trebuchet MS bold", 24),bg='white')
    min2.place(relx=0.7, rely=0.2, relwidth=0.2, relheight=0.5)

    enterClock = Button(newWindow,
                        relief=FLAT,
                        text='Set a reminder',
                        font=("Trebuchet MS bold", 24),
                        background='#122faa',
                        command=start_timer)
    enterClock.place(relx=0, rely=0.7, relwidth=1, relheight=0.3)

header = tk.Frame(window,
                  background='white')

greating = tk.Label(header,
                    text="    Good evening, User",
                    background='white',
                    font=("Trebuchet MS bold", 24),
                    anchor='w')

lists = tk.Frame(window,
                background='white')

main = tk.Frame(window,
                background='white',bd=1, relief="groove")

add = tk.Frame(main,
                background='white')

background_image = tk.PhotoImage(file="ico4.png")

add1 = Button(add,
              relief=FLAT,
              image=background_image,
              background='white',command=addlabel)

add2 = Entry(add)

ico5 = PhotoImage(file="ico5.png")

add3 = Button(add,
                relief=FLAT,
                 image=ico5,
                 background='white',
                 command=timer1)

dateDAY = tk.Frame(main,
                background='white')

dateDAY1 = tk.Label(dateDAY,
                text=dick1[str(weekday)],
                font=("Trebuchet MS bold", 12),
                 background='white')
dateDAY2 = tk.Label(dateDAY,
                text=the_day,
                font=("Trebuchet MS bold", 28),
                 background='white')
dateDAY3 = tk.Label(dateDAY,
                text=dick2[str(month)],
                font=("Trebuchet MS bold", 12),
                 background='white')

things = tk.Frame(main,
                background='#f7f7f7')

llists = Frame(lists,
            background='white')

today = Frame(llists,
              background='white')

today2 = Button(today,
                relief=FLAT,
                 text="Today",
                 background='white',
                command=lambda: buttonClickWEEK(the_day))

week = Frame(llists,
              background='purple')

week2 = Button(week,
                relief=FLAT,
                 text="Next 5 days",
                 background='white',
                command=lambda: frameWEEK.tkraise())

separator1 = ttk.Separator(window, orient='horizontal')
separator2 = ttk.Separator(window, orient='vertical')

ico1 = PhotoImage(file="ico1.png")
ico1_label = Label(header, background='white', image=ico1)

ico2 = PhotoImage(file="ico2.png")
today1 = Label(today, image=ico2, background='white')

ico3 = PhotoImage(file="ico3.png")
week1 = Label(week, image=ico3, background='white')

header.place(relwidth=1, relheight=0.2)
greating.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
ico1_label.place(relx=0, rely=0, relwidth=0.2, relheight=1)
lists.place(relx=0, rely=0.2, relwidth=0.2, relheight=0.8)
main.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)
separator1.place(relx=0, rely=0.2, relwidth=1, relheight=0.0000001)
separator2.place(relx=0.2, rely=0, relwidth=0.0000001, relheight=1)
add.place(relx=0.2, rely=0.9, relwidth=0.75, relheight=0.075)
add1.place(relx=0, rely=0, relwidth=0.075, relheight=1)
add2.place(relx=0.075, rely=0, relwidth=0.85, relheight=1)
add3.place(relx=0.925, rely=0, relwidth=0.075, relheight=1)
dateDAY.place(relx=0.01, rely=0.02, relwidth=0.15, relheight=0.2)
dateDAY1.place(relx=0, rely=0, relwidth=1, relheight=0.2)
dateDAY2.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)
dateDAY3.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)
things.place(relx=0.2, rely=0.02, relwidth=0.75, relheight=0.85)
llists.place(relx=0.1, rely=0.02, relwidth=0.8, relheight=0.85)
today.place(relx=0, rely=0, relwidth=1, relheight=0.085)
today1.place(relx=0, rely=0, relwidth=0.2, relheight=1)
today2.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
week.place(relx=0, rely=0.085, relwidth=1, relheight=0.085)
week1.place(relx=0, rely=0, relwidth=0.2, relheight=1)
week2.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

main.tkraise()
buttonClickWEEK(the_day)
window.mainloop()
conn.close()
