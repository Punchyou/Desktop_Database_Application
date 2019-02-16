# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 17:31:17 2019

@author: Maria
"""

import sqlite3

class Database:
    
    def __init__(self, db):
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year interger, isbn integer)")
        conn.commit()
        conn.close()

    #insert the data
    def insert(self, title, author, year, isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        conn.commit()
        conn.close()
    
    #fetch the data
    def view(self):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        conn.close()
        return rows
    
    #search func
    def search(self, title = "", author = "", year = "", isbn = ""):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT *  FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
        rows = cur.fetchall()
        conn.close()
        return rows
    
    #delete a record
    def delete(self, id):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id = ?", (id,))
        conn.commit()
        conn.close()
    
    #update a record
    def update(self, id, title, author, year, isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
        conn.commit()
        conn.close()