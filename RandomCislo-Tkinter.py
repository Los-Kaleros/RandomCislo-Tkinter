from tkinter import *
from tkinter import font
import random
from tkinter import Listbox


def vysledok():
    value = print(random.randint(0, 10))
    return value
 




app = Tk()
app.geometry("450x400")
app.title("RandomNumber")
app.resizable(False, False)
app.config(bg="#14e4ff")


frame = Frame(app)
frame.pack(pady=15)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)


    

btn_frame = Frame(app)
btn_frame.pack(pady=15)

start_btn = Button(
    btn_frame,
    text = "START",
    font = ("times 14"),
    bg= "grey",
    command=vysledok,

)
start_btn.pack(fill=BOTH, expand=TRUE, side=TOP)





app.mainloop()
