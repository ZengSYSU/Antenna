# -*- coding: utf-8 -*-
from tkinter import Tk, Label, StringVar, Entry, Button, Frame, TOP
import main

root = Tk()
root.title('最佳喇叭计算 by kuangzl')
root.geometry('420x280')
root.resizable(width=False, height=False)

tip = Label(root, text='由波束宽度计算喇叭尺寸，\n使得该尺寸下增益最大化', height=3,
            font=('Microsoft YaHei UI', 12, 'italic'))
tip.pack(side=TOP)

frm = Frame(root)
frm.pack()

Label(frm, text='中频(GHz):').grid(row=0, column=0)
Label(frm, text='E面(deg):').grid(row=1, column=0)
Label(frm, text='H面(deg):').grid(row=2, column=0)
Label(frm, text='波导宽(mm):').grid(row=0, column=2)
Label(frm, text='波导窄(mm):').grid(row=1, column=2)
Label(frm, text='喇叭宽(mm):').grid(row=2, column=2)
Label(frm, text='喇叭窄(mm):').grid(row=3, column=2)
Label(frm, text='喇叭长(mm):').grid(row=4, column=2)


def calc():
    f = float(v1.get())
    E = float(v2.get())
    H = float(v3.get())
    horn = main.Horn(f, E, H)
    horn.para()
    v4.set(horn.wg_a)
    v5.set(horn.wg_b)
    v6.set(horn.horn_a)
    v7.set(horn.horn_b)
    v8.set(horn.horn_l)


def hfss():
    f = float(v1.get())
    E = float(v2.get())
    H = float(v3.get())
    horn = main.Horn(f, E, H)
    horn.para()
    horn.realize_in_hfss()


v1 = StringVar()
Entry(frm, textvariable=v1, width=8).grid(row=0, column=1, padx=10, pady=5)
v2 = StringVar()
Entry(frm, textvariable=v2, width=8).grid(row=1, column=1, padx=10, pady=5)
v3 = StringVar()
Entry(frm, textvariable=v3, width=8).grid(row=2, column=1, padx=10, pady=5)


v4 = StringVar()
Label(frm, textvariable=v4, width=10).grid(row=0, column=3)
v5 = StringVar()
Label(frm, textvariable=v5, width=10).grid(row=1, column=3)
v6 = StringVar()
Label(frm, textvariable=v6, width=10).grid(row=2, column=3)
v7 = StringVar()
Label(frm, textvariable=v7, width=10).grid(row=3, column=3)
v8 = StringVar()
Label(frm, textvariable=v8, width=10).grid(row=4, column=3)

Button(frm, text='calc', command=calc).grid(row=4, column=0)
Button(frm, text='hfss', command=hfss).grid(row=4, column=1)

root.mainloop()
