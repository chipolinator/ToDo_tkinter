from tkinter import *
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import font
#122faa



window = Tk()
window.title("Neva")
#window.resizable(width=False, height=False)
window.iconbitmap('1.ico')
window.geometry("1000x700")

weekday = datetime.now().weekday()
the_day = datetime.now().day
month = datetime.now().month

dick1 = {'0':'Sunday','1':'Monday','2':'Tuesday','3':'Wednesday','4':'Thursday','5':'Friday','6':'Saturday'}
dick2 = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}

enabled = IntVar()

lblist = []


def on_checked(button):
    if button["bg"] == "white":
        button['font'] = font.Font(family= "Trebuchet MS ", size=12, overstrike=True)
        button.config(bg="gray")

    else:
        button['font'] = font.Font(family= "Trebuchet MS ", size=12, overstrike=False)
        button.config(bg="white")


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
    res.place(relx=0, rely=0.125*(len(lblist)), relwidth=1, relheight=0.1)
    lblist.append(res)
    add2.delete(0, END)



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
                background='white')

add = tk.Frame(main,
                background='white')


background_image=tk.PhotoImage(file="ico4.png")

add1 = Button(add,
              relief=FLAT,
              image=background_image,
              background='white',command=addlabel)

add2 = Entry(add)

ico5 = PhotoImage(file="ico5.png")

add3 = Button(add,
                relief=FLAT,
                 image=ico5,
                 background='white')
                 #command=a)



date = tk.Frame(main,
                background='white')

date1 = tk.Label(date,
                text=dick1[str(weekday)],
                font=("Trebuchet MS bold", 12),
                 background='white')
date2 = tk.Label(date,
                text=the_day,
                font=("Trebuchet MS bold", 28),
                 background='white')
date3 = tk.Label(date,
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
                 background='white')
                 #command=a)

week = Frame(llists,
              background='purple')


week2 = Button(week,
                relief=FLAT,
                 text="Week",
                 background='white')
                 #command=a)

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
date.place(relx=0.01, rely=0.02, relwidth=0.15, relheight=0.2)
date1.place(relx=0, rely=0, relwidth=1, relheight=0.2)
date2.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)
date3.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)
things.place(relx=0.2, rely=0.02, relwidth=0.75, relheight=0.85)
llists.place(relx=0.1, rely=0.02, relwidth=0.8, relheight=0.85)
today.place(relx=0, rely=0, relwidth=1, relheight=0.085)
today1.place(relx=0, rely=0, relwidth=0.2, relheight=1)
today2.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
week.place(relx=0, rely=0.085, relwidth=1, relheight=0.085)
week1.place(relx=0, rely=0, relwidth=0.2, relheight=1)
week2.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

window.mainloop()