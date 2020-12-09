# -*- coding: utf-8 -*-
from tkinter import Tk, Label, StringVar, Entry, Button, Frame
import main128

root = Tk()
root.title('阵列天线')
root.geometry('480x360')
root.resizable(width=False, height=False)

frm = Frame(root)
frm.pack()

Label(frm, text='中频(GHz):').grid(row=0, column=0)
Label(frm, text='阵元间距X(mm):').grid(row=1, column=0)
Label(frm, text='阵元间距Y(mm):').grid(row=2, column=0)


def hfss():
    f = float(v1.get())
    ud = float(v2.get())
    vd = float(v3.get())
    array = main128.Array(f, ud, vd)
    array.call_hfss()


v1 = StringVar()
Entry(frm, textvariable=v1, width=8).grid(row=0, column=1, padx=10, pady=5)
v2 = StringVar()
Entry(frm, textvariable=v2, width=8).grid(row=1, column=1, padx=10, pady=5)
v3 = StringVar()
Entry(frm, textvariable=v3, width=8).grid(row=2, column=1, padx=10, pady=5)

Button(frm, text='hfss', command=hfss).grid(row=5, column=0)


root.mainloop()