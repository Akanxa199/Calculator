import tkinter
from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()
root.geometry("400x500+400+30")
root.resizable(0, 0)
root.title("Calculator")

val = ""
A = 0
Opretor = ""

# Functions :

# Event For 1 to 9


def Onclick0():
    global val
    val = val + "0"
    data.set(val)


def Onclick1():
    global val
    val = val + "1"
    data.set(val)


def Onclick2():
    global val
    val = val + "2"
    data.set(val)


def Onclick3():
    global val
    val = val + "3"
    data.set(val)


def Onclick4():
    global val
    val = val + "4"
    data.set(val)


def Onclick5():
    global val
    val = val + "5"
    data.set(val)


def Onclick6():
    global val
    val = val + "6"
    data.set(val)


def Onclick7():
    global val
    val = val + "7"
    data.set(val)


def Onclick8():
    global val
    val = val + "8"
    data.set(val)


def Onclick9():
    global val
    val = val + "9"
    data.set(val)

# for Opretors


def Onclick_plus():
    global val, A, Opretor
    A = int(val)
    Opretor = "+"
    val = val + "+"
    data.set(val)


def Onclick_minus():
    global val, A, Opretor
    A = int(val)
    Opretor = "-"
    val = val + "-"
    data.set(val)


def Onclick_multiply():
    global val, A, Opretor
    A = int(val)
    Opretor = "*"
    val = val + "*"
    data.set(val)


def Onclick_devide():
    global val, A, Opretor
    A = int(val)
    Opretor = "/"
    val = val + "/"
    data.set(val)


def Onclick_C():
    global val, A, Opretor
    A = ""
    Opretor = ""
    val = ""
    data.set(val)

# For Result


def Onclick_equl():
    global val, opretor, A
    val2 = val
    if Opretor == "+":
        x = int(((val2.split("+"))[1]))
        res = A + x
        data.set(res)
        val = str(res)
    elif Opretor == "-":
        x = int(((val2.split("-"))[1]))
        res = A - x
        data.set(res)
        val = str(res)
    elif Opretor == "*":

        x = int(((val2.split("*"))[1]))
        res = A * x
        data.set(res)
        val = str(res)
    elif Opretor == "/":
        x = int(((val2.split("/"))[1]))
        if A == 0:
            data.set("ERROR")
            messagebox.showerror("Error", "Devide By Zero Is Not possible")
            data.set("")
        else:
            res = A / x
            data.set(int(res))
            val = str(res)


data = StringVar()
lbl = Label(
    root,
    font=("vernada", 20),
    textvariable=data,
    background="#ffffff",
    fg="#000000",
    text="Hello",
    anchor=SE,
)
lbl.pack(expand=True, fill="both")

# Frame1(It Includes Buttons Of Row 1)
frame1 = Frame(root)
frame1.pack(expand=True, fill="both")

btn1 = Button(
    frame1,
    text="1",
    font=("verdana", 22),
    border=0,
    relief=GROOVE,
    command=Onclick1,
)
btn1.pack(side=LEFT, expand=True, fill="both")
btn2 = Button(
    frame1,
    text="2",
    font=("verdana", 22),
    border=0,
    relief=GROOVE,
    command=Onclick2
)
btn2.pack(side=LEFT, expand=True, fill="both")
btn3 = Button(
    frame1,
    text="3",
    font=("verdana", 22),
    border=0,
    relief=GROOVE,
    command=Onclick3
)
btn3.pack(side=LEFT, expand=True, fill="both")
btn_plus = Button(
    frame1,
    text="+",
    font=("verdana", 25),
    border=0,
    relief=GROOVE,
    command=Onclick_plus
)
btn_plus.pack(side=LEFT, expand=True, fill="both")

# Frame2(It Includes Buttons Of Row 2)
frame2 = Frame(root)
frame2.pack(expand=True, fill="both")

btn4 = Button(
    frame2,
    text="4",
    font=("verdana", 22),
    border=0,
    relief=GROOVE,
    command=Onclick4
)
btn4.pack(side=LEFT, expand=True, fill="both")
btn5 = Button(
    frame2,
    text="5",
    font=("verdana", 22),
    border=0,
    relief=GROOVE,
    command=Onclick5
)
btn5.pack(side=LEFT, expand=True, fill="both")
btn6 = Button(
    frame2,
    text="6",
    font=("verdana", 22),
    border=0,
    relief=GROOVE,
    command=Onclick6
)
btn6.pack(side=LEFT, expand=True, fill="both")
btn_minus = Button(
    frame2,
    text="-",
    font=("verdana", 25),
    border=0,
    relief=GROOVE,
    command=Onclick_minus
)
btn_minus.pack(side=LEFT, expand=True, fill="both")

# Frame3(It Includes Buttons Of Row 3)
frame3 = Frame(root)
frame3.pack(expand=True, fill="both")

btn7 = Button(
    frame3,
    text="7",
    font=("verdana", 22),
    border=0,
    relief=GROOVE,
    command=Onclick7
)
btn7.pack(side=LEFT, expand=True, fill="both")
btn8 = Button(
    frame3,
    text="8",
    font=("verdana", 22),
    border=0,
    relief=GROOVE,
    command=Onclick8
)
btn8.pack(side=LEFT, expand=True, fill="both")
btn9 = Button(
    frame3,
    text="9",
    font=("verdana", 22),
    border=0,
    relief=GROOVE,
    command=Onclick9
)
btn9.pack(side=LEFT, expand=True, fill="both")
btn_multiply = Button(
    frame3,
    text="*",
    font=("verdana", 25),
    border=0,
    relief=GROOVE,
    command=Onclick_multiply
)
btn_multiply.pack(side=LEFT, expand=True, fill="both")

# Frame4(It Includes Buttons Of Row 4)
frame4 = Frame(root)
frame4.pack(expand=True, fill="both")

btn_C = Button(
    frame4,
    text="C",
    font=("verdana", 22),
    border=0,
    relief=GROOVE,
    command=Onclick_C
)
btn_C.pack(side=LEFT, expand=True, fill="both")
btn0 = Button(
    frame4,
    text="0",
    font=("verdana", 22),
    border=0,
    relief=GROOVE,
    command=Onclick0
)
btn0.pack(side=LEFT, expand=True, fill="both")
btn_equl = Button(
    frame4,
    text="=",
    font=("verdana", 25),
    border=0,
    relief=GROOVE,
    command=Onclick_equl
)
btn_equl.pack(side=LEFT, expand=True, fill="both")

btn_devide = Button(
    frame4,
    text="/",
    font=("verdana", 25),
    border=0,
    relief=GROOVE,
    command=Onclick_devide
)
btn_devide.pack(side=LEFT, expand=True, fill="both")

root.mainloop()
