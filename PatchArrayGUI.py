# -*- coding: utf-8 -*-
from tkinter import Tk, Label, StringVar, Entry, Button, Frame
import PatchArrayMain

root = Tk()
root.title('尾杆天线')
root.geometry('360x280')
root.resizable(width=False, height=False)

frm = Frame(root)
frm.pack()

Label(frm, text='中频(GHz):').grid(row=0, column=0)
Label(frm, text='幅度(W):').grid(row=1, column=0)
Label(frm, text='相位(deg):').grid(row=3, column=0)


def hfss():
    f = float(v1.get())
    p1 = float(v2.get())
    p2 = float(v3.get())
    p3 = float(v4.get())
    p4 = float(v5.get())
    f1 = float(v6.get())
    f2 = float(v7.get())
    f3 = float(v8.get())
    f4 = float(v9.get())
    patch = PatchArrayMain.PatchArray(f, [p1, p2, p3, p4], [f1, f2, f3, f4])
    patch.size()
    patch.call_hfss()


v1 = StringVar()
Entry(frm, textvariable=v1, width=8).grid(row=0, column=1, padx=10, pady=5)
v2 = StringVar()
Entry(frm, textvariable=v2, width=8).grid(row=1, column=1, padx=10, pady=5)
v3 = StringVar()
Entry(frm, textvariable=v3, width=8).grid(row=1, column=2, padx=10, pady=5)
v4 = StringVar()
Entry(frm, textvariable=v4, width=8).grid(row=2, column=1, padx=10, pady=5)
v5 = StringVar()
Entry(frm, textvariable=v5, width=8).grid(row=2, column=2, padx=10, pady=5)
v6 = StringVar()
Entry(frm, textvariable=v6, width=8).grid(row=3, column=1, padx=10, pady=5)
v7 = StringVar()
Entry(frm, textvariable=v7, width=8).grid(row=3, column=2, padx=10, pady=5)
v8 = StringVar()
Entry(frm, textvariable=v8, width=8).grid(row=4, column=1, padx=10, pady=5)
v9 = StringVar()
Entry(frm, textvariable=v9, width=8).grid(row=4, column=2, padx=10, pady=5)
Button(frm, text='hfss', command=hfss).grid(row=5, column=0)

root.mainloop()
