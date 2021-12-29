from tkinter import *
from tkinter import font


app = Tk()
app.geometry("450x400")
app.title("RandomNumber")
app.resizable(False, False)
app.config(bg="#14e4ff")

frame = Frame(app)
frame.pack(pady=15)

btn_frame = Frame(app)
btn_frame.pack(pady=15)

start_btn = Button(
    btn_frame,
    text = "START",
    font = ("times 14"),
    bg= "grey",

)
start_btn.pack(fill=BOTH, expand=TRUE)


app.mainloop()