# -*- coding: utf-8 -*-
from tkinter import Tk, Label, StringVar, Entry, Button, Frame
import PatchMain

root = Tk()
root.title('微带天线')
root.geometry('360x280')
root.resizable(width=False, height=False)

frm = Frame(root)
frm.pack()

Label(frm, text='中频(GHz):').grid(row=0, column=0)


def hfss():
    f = float(v1.get())
    micro = PatchMain.MicroStrip(f)
    micro.call_hfss()


v1 = StringVar()
Entry(frm, textvariable=v1, width=8).grid(row=0, column=1, padx=10, pady=5)
Button(frm, text='hfss', command=hfss).grid(row=2, column=0)

root.mainloop()
