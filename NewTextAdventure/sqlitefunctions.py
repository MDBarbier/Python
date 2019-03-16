#!/usr/bin/python
# -*- coding: utf-8 -*-


import sqlite3 as lite
import sys

def CreateSqliteConnection(db_file):
    try:
        conn = lite.connect(db_file)
        return conn
    except Exception as e:
        print(e)
    return None

def CheckSqliteVersion():
    conn = None
    try:
        conn = lite.connect('test.db')
        cur = conn.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        return data
    except Exception as e:
        print("Error: %s" % e.args[0])
    finally:
        if conn:
            conn.close()

def InsertPlayer(player):
    conn = None
    sql = '''
            INSERT INTO player_data (name, shortname, password) 
            VALUES(?,?,?)'''
    try:
        conn = CreateSqliteConnection('test.db')
        cursor = conn.cursor()
        cursor.execute(sql, player)
    except Exception as e:
        print("Cannot create player: %s", e)
    finally:
        if conn:
            conn.close()

    print("player created with id %s" % cursor.lastrowid)
    conn.commit()
    conn.close()

def CheckCredentialsAgainstDatabase(usernameToCheck, passwordToCheck):
    conn = None
    sql = "SELECT * FROM player_data WHERE name = '{0}' AND password = '{1}'".format(usernameToCheck, passwordToCheck)
    conn = CreateSqliteConnection('test.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    theRow = rows[0]
    if theRow[0] == usernameToCheck and theRow[2] == passwordToCheck:
        return True
    else:
        return False