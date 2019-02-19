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
from backend import Database

class Window(object):
    def __init__(self, window):
        self.window = window
        self.window.wm_title("BookStore")

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
        self.title_text = StringVar()
        self.e1 = Entry(window, textvariable = self.title_text)
        self.e1.grid(row = 0, column = 1)
        
        self.author_text = StringVar()
        self.e2 = Entry(window, textvariable = author_text)
        self.e2.grid(row = 0, column = 3)
        
        self.year_text = StringVar()
        self.e3 = Entry(window, textvariable = year_text)
        self.e3.grid(row = 1, column = 1)
        
        self.isbn_text = StringVar()
        self.e4 = Entry(window, textvariable = isbn_text)
        self.e4.grid(row = 1, column = 3)
        
        #create list
        self.list1 = Listbox(window, height = 6, width = 35)
        self.list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)
        
        #bind a method to the widget
        self.list1.bind("<<ListboxSelect>>", self.get_selected_row)
        
        #create scrollbar
        sb1 = Scrollbar(window)
        sb1.grid(row = 2, column = 2, rowspan = 6)
        
        #confidure schrollbar
        self.list1.configure(yscrollcommand = sb1.set)
        sb1.configure(command=list1.yview)
        
        #create button
        b1 = Button(window, text = "View all", width = 12, command = self.view_command)
        b1.grid(row = 2, column = 3)
        
        b2 = Button(window, text = "Search entry", width = 12, command = self.search_command)
        b2.grid(row = 3, column = 3)
        
        b3 = Button(window, text = "Add entry", width = 12, command = self.add_command)
        b3.grid(row = 4, column = 3)
        
        b4 = Button(window, text = "Update entry", width = 12, command = self.update_command)
        b4.grid(row = 5, column = 3)
        
        b5 = Button(window, text = "Delete selected", width = 12, command = self.delete_command)
        b5.grid(row = 6, column = 3)
        
        b6 = Button(window, text = "Close", width = 12, command = window.destroy)
        b6.grid(row = 7, column = 3)
        
        #select the row we want to delete
    def get_selected_row(self, event):
        self.index = list1.curselection()[0] #[0] to get single numbers (it's a tuple)
        self.selected_tuple = list1.get(index)
        
        #fill the entries when the user selects a row
        self.e1.delete(0, END)
        self.e1.insert(END, selected_tuple[1])
        self.e2.delete(0, END)
        self.e2.insert(END, selected_tuple[2])
        self.e3.delete(0, END)
        self.e3.insert(END, selected_tuple[3])
        self.e4.delete(0, END)
        self.e4.insert(END, selected_tuple[4])

    def view_command(self):
        self. list1.delete(0, END) #clear the list before insert anything
        for row in database.view():
            self.list1.insert(END, row) #new rows will be inserted at the end of the row
        
    def search_command(self):
        list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):#get() to produce a string
            self.list1.insert(END, row)
    
    def add_command(self):
        database.insert(self.title_text.get(),self. author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
        
    def delete_command(self):
        database.delete(self.selected_tuple[0])
        
    def update_command(self):
        database.update(self.selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

database = Database("books.db")

window = Tk()
Window(window)
window.mainloop()