#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sqlite3 as lite
import sys

def createTables(conn, create_tables_sql):    
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_tables_sql)
    except Error as e:
        print(e)

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = lite.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
 
def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    print("in create project method")
    sql = "INSERT INTO projects(name,begin_date,end_date) VALUES(?,?,?)"
    #sql = "INSERT INTO projects(name,begin_date,end_date) VALUES('?','?','?')"
    cur = conn.cursor()
    cur.execute(sql, project)
    print("project creation method completed")
    return cur.lastrowid

def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
 
    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid

def select_all_projects(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM projects")
 
    rows = cur.fetchall()
 
    print("Printing all rows:")
    for row in rows:
        print(row)

def main():
    print("main executing")

    database = "C:\\Users\\matth\\Documents\\GitHub\\Python\\sqlite-demo\\test.db"
 
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """
 
    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""
    
    con = None
 
    try:
        con = lite.connect('test.db')
        cur = con.cursor()    
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        print("SQLite version: %s" % data)
    except Exception as e:   
        print("Error %s:" % e.args[0])
        sys.exit(1)
    finally:    
        if con:
            con.close()

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        #createTables(conn, sql_create_projects_table)
        # create tasks table
        #createTables(conn, sql_create_tasks_table)
         # tasks
        
        # create a new project
        project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30')
        project_id = create_project(conn, project)

        #print("projectID: " + str(project_id))
        #task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        #task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

        # create tasks
        #create_task(conn, task_1)
        #create_task(conn, task_2)
        select_all_projects(conn)

        conn.commit()
        conn.close()
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()