# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 17:31:17 2019

@author: Maria
"""

import sqlite3

class Database:
    
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year interger, isbn integer)")
        self.conn.commit()

    #insert the data
    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.conn.commit()
    
    #fetch the data
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows
    
    #search func
    def search(self, title = "", author = "", year = "", isbn = ""):
        self.cur.execute("SELECT *  FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows
    
    #delete a record
    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id = ?", (id,))
    
    #update a record
    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
        