from tkinter import *
import tkinter as tk

window = Tk()
window.title("To do")
window.resizable(width=False, height=False)
window.iconbitmap('1.ico')
window.geometry("1000x700")


header = tk.Frame(window,
                  background='red')

greating = tk.Label(header,
                    text="Good evening, user",
                    background='red',
                    font=("Trebuchet MS bold", 24))

lists = tk.Frame(window,
                background='orange')

main = tk.Frame(window,
                background='blue')

add = tk.Frame(main,
                background='green')

add1 = Button(add,
                text="+",
                 background='white')
                 #command=a)

add2 = Entry(add)


date = tk.Frame(main,
                background='purple')

date1 = tk.Label(date,
                text="FRI",
                font=("Trebuchet MS bold", 12))
date2 = tk.Label(date,
                text="28",
                font=("Trebuchet MS bold", 28))
date3 = tk.Label(date,
                text="April",
                font=("Trebuchet MS bold", 12))

things = tk.Frame(main,
                background='white')

llists = Frame(lists,
            background='blue')

today = Frame(llists,
              background='gray')

today2 = Button(today,
                 text="Today",
                 background='white')
                 #command=a)

week = Frame(llists,
              background='purple')


week2 = Button(week,
                 text="Week",
                 background='white')
                 #command=a)


ico1 = PhotoImage(file="ico1.png")
ico1 = ico1.subsample(5, 5)
ico1_label = Label(header)
ico1_label.image = ico1
ico1_label['image'] = ico1_label.image

ico2 = PhotoImage(file="ico2.png")
ico2 = ico2.subsample(5, 5)
today1 = Label(today)
today1.image = ico2
today1['image'] = today1.image

ico3 = PhotoImage(file="ico3.png")
ico3 = ico3.subsample(5, 5)
week1 = Label(week)
week1.image = ico3
week1['image'] = week1.image


header.place(relwidth=1, relheight=0.2)
greating.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
ico1_label.place(relx=0, rely=0, relwidth=0.2, relheight=1)
lists.place(relx=0, rely=0.2, relwidth=0.2, relheight=0.8)
main.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)
add.place(relx=0.2, rely=0.9, relwidth=0.75, relheight=0.1)
add1.place(relx=0, rely=0, relwidth=0.1, relheight=1)
add2.place(relx=0.1, rely=0, relwidth=0.9, relheight=1)
date.place(relx=0.01, rely=0.01, relwidth=0.15, relheight=0.2)
date1.place(relx=0, rely=0, relwidth=1, relheight=0.2)
date2.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)
date3.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)
things.place(relx=0.2, rely=0.01, relwidth=0.75, relheight=0.85)
llists.place(relx=0.14, rely=0.01, relwidth=0.75, relheight=0.85)
today.place(relx=0, rely=0, relwidth=1, relheight=0.1)
today1.place(relx=0, rely=0, relwidth=0.2, relheight=1)
today2.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
week.place(relx=0, rely=0.1, relwidth=1, relheight=0.1)
week1.place(relx=0, rely=0, relwidth=0.2, relheight=1)
week2.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)


window.mainloop()