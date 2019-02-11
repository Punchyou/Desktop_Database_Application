# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 21:27:54 2019

@author: Maria
"""
from tkinter import *
window = Tk()
def km_to_miles():
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)
    
#create button
b1 = Button(window, text="Execute", command= km_to_miles)
b1.grid(row = 0, column = 0, rowspan = 2)

#create an entry
e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)

#text
t1 = Text(window, height = 1, width = 20)
t1.grid(row = 0, column = 2)
window.mainloop()