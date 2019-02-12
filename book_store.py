# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 22:07:41 2019

@author: Maria
"""

"""
A programm that stores this book information
Title, Author
Year, ISBN

The user can:
    View all records
    Search an entry
    Add entry
    Update entry
    Delete
    Close
    """
    
from tkinter import *

window = Tk()

#create labels
l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Author")
l2.grid(row = 0, column = 2)

l2 = Label(window, text = "Year")
l2.grid(row = 1, column = 0)

l2 = Label(window, text = "ISBN")
l2.grid(row = 1, column = 2)

#create entry
title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 3)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)

isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text)
e4.grid(row = 1, column = 3)

#create list
list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

#create scrollbar
sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)

#confidure schrollbar
list1.configure(yscrollcommand = sb1.set)
sb1.configure(command=list1.yview)

#create button
b1 = Button(window, text = "View all", width = 12)
b1.grid(row = 2, column = 3)

b1 = Button(window, text = "Search entry", width = 12)
b1.grid(row = 3, column = 3)

b1 = Button(window, text = "Add entry", width = 12)
b1.grid(row = 4, column = 3)

b1 = Button(window, text = "Update entry", width = 12)
b1.grid(row = 5, column = 3)

b1 = Button(window, text = "Delete selected", width = 12)
b1.grid(row = 6, column = 3)

window.mainloop()