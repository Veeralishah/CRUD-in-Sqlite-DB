#-*- coding: utf8 -*-


import db_config
import sqlite3 as sdb
import sys
import warnings





''' SQLITE CRUD '''

# CREATE A NEW TABLE


def createTable_sqlite(con):
    with con:

        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Student")
        cur.execute("CREATE TABLE Student(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(25),College VARCHAR(25), Course VARCHAR(25), Age INT, City VARCHAR(25));")
        print 'Student Table created'

# # INSERT VALUES


def insertTable_sqlite(con):
    with con:

        try:
            cur = con.cursor()

            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS Student(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(25),College VARCHAR(25), Course VARCHAR(25), Age INT, City VARCHAR(25));")
                warnings.filterwarnings('ignore', 'unknown table')

            Name = raw_input("Enter Your Name ")
            College = raw_input("Enter Your College Name")
            Course = raw_input("Enter Your Course")
            Age = raw_input("Enter Your Age")
            City = raw_input("Enter Your City")
            cur.execute("INSERT INTO Student(Name, College, Course, Age, City) VALUES (?, ?, ?, ?, ?)",
                        (Name, College, Course, Age, City))
            print "Record Inserted"
        except Exception as e:
            print e


# RETRIEVE TABLE ROWS
def retrieveTable_sqlite(con):
    with con:

        cur = con.cursor()
        con.row_factory = sdb.Row
        cur.execute("SELECT * FROM Student")

        rows = cur.fetchall()
        for row in rows:
            if row == None:
                print 'Please Insert Record'
                break
            else:
                print('ID: {0} Name: {1} College: {2} Course: {3} Age: {4} City: {5}'.format(
                    row[0], row[1], row[2], row[3], row[4], row[5]))


# # UPDATE ROW
def updateRow_sqlite(con):
    with con:

        try:
            cur = con.cursor()
            con.row_factory = sdb.Row
            cur.execute("SELECT * FROM Student")
            rows = cur.fetchall()
            for row in rows:
                print('ID: {0} Name: {1} College: {2} Course: {3} Age: {4} City: {5}'.format(
                    row[0], row[1], row[2], row[3], row[4], row[5]))

            id = input("Enter ID for Update Record")
            name = raw_input("Enter Name for Update Record")
            clgname = raw_input("Enter College Name for Update Record")
            csr = raw_input("Enter Course for Update Record")
            age = raw_input("Enter Age for Update Record")
            city = raw_input('Enter City Name For Update record')
            cur.execute("UPDATE Student SET Name = ?, College = ?, Course = ?, Age = ?, City = ?  WHERE Id = ?",
                        (name, clgname, csr, age, city, id))
            print "Number of rows updated:",  cur.rowcount
            if cur.rowcount == 0:
                print 'Record Not Updated'
        except TypeError as e:
            print 'ID Not Exist '

#  DELETE ROW


def deleteRow_sqlite(con):
    with con:

        try:
            cur = con.cursor()
            con.row_factory = sdb.Row
            cur.execute("SELECT * FROM Student")
            rows = cur.fetchall()
            for row in rows:
                print 'Table Data:', row["Id"], row["Name"], row["College"], row["Course"], row["Age"], row["City"]

            id = input("Enter ID for Delete Record")
            cur.execute("DELETE FROM Student WHERE Id =  ?", (id,))
            print "Number of rows deleted:", cur.rowcount

        except TypeError as e:
            print 'ID Not Exist '
