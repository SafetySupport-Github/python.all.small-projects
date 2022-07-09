# Thanks noverd for an original project

from tkinter import *
from tkinter.ttk import Combobox

def Run():
    global user, password, u_to_report, combo, intrep, window
    from scratchclient import ScratchSession
    s = ScratchSession(user.get(), password.get())
    c = s.get_user(u_to_report.get())
    x = combo.get()
    while int(intrep.get()):
        try:
            c.report(x)
        except:
            pass
    window.destroy()

window = Tk()
window.title("Массрепортер")
window.geometry('900x300')
l3 = Label(window, text="Ник спамера", font=("Arial Bold", 10))
user = Entry(window, width=20)
l4 = Label(window, text="Пароль спамера", font=("Arial Bold", 10))
password = Entry(window, width=20)
l5 = Label(window, text="Ник цели", font=("Arial Bold", 10))
u_to_report = Entry(window, width=20)
l6 = Label(window, text="Тип Жалобы", font=("Arial Bold", 10))
intrep=Entry(window, width=5)
l7 = Label(window, text="Количество репортов", font=("Arial Bold", 10))
b = Button(window, command=Run, text="Атаковать")
combo = Combobox(window)
combo["values"] = ("Username",
                   "Icon",
                   "About Me",
                   "What I'm Working On")

l3.pack()
user.pack()
l4.pack()
password.pack()
l5.pack()
u_to_report.pack()
l6.pack()
combo.pack()
l7.pack()
intrep.pack()
b.pack()

window.mainloop()
