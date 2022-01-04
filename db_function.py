import sqlite3
#import cv2

conn = sqlite3.connect("data.db", check_same_thread = False)
c = conn.cursor()
 
# Database
# tABLE
# field/ columns
# Data Type


# Creaating the table for the Personal development
def create_table_personal_development():
    c.execute('CREATE TABLE IF NOT EXISTS personaltasktable(task TEXT, reason TEXT, impact TEXT, task_status TEXT, task_start_date DATE, task_due_date DATE, time TEXT)')

def add_task_personal_development(task, reason, impact, task_status, task_start_date, task_due_date, time):
    c.execute('INSERT INTO personaltasktable(task, reason, impact, task_status, task_start_date, task_due_date, time) VALUES (?,?, ?, ?, ?, ?,?)', (task, reason, impact, task_status, task_start_date, task_due_date, time))
    conn.commit()
    
def view_all_data_personal():
    c.execute('SELECT * FROM personaltasktable')
    data = c.fetchall()
    return data
    
    
# creating the tables for the career 
def create_table_career():
    c.execute('CREATE TABLE IF NOT EXISTS personaltasktable(task TEXT, reason TEXT, impact TEXT, task_status TEXT, task_start_date DATE, task_due_date DATE)')
    
def add_task_career(task, reason, impact, task_status, task_start_date, task_due_date):
    c.execute('INSERT INTO careertasktable(task, reason, impact, task_status, task_start_date, task_due_date) VALUES (?,?, ?, ?, ?, ?)', (task, reason, impact, task_status, task_start_date, task_due_date))
    conn.commit()

def view_all_data_career():
    c.execute('SELECT * FROM careertasktable')
    data = c.fetchall()
    return data
    
# creating the tables for the Business 
def create_table_business():
    c.execute('CREATE TABLE IF NOT EXISTS personaltasktable(task TEXT, reason TEXT, impact TEXT, task_status TEXT, task_start_date DATE, task_due_date DATE)')
    
def add_task_business(task, reason, impact, task_status, task_start_date, task_due_date):
    c.execute('INSERT INTO businesstasktable(task, reason, impact, task_status, task_start_date, task_due_date) VALUES (?,?, ?, ?, ?, ?)', (task, reason, impact, task_status, task_start_date, task_due_date))
    conn.commit()
    
def view_all_data_business():
    c.execute('SELECT * FROM businesstasktable')
    data = c.fetchall()
    return data
    
# creating the tables for the family 
def create_table_family():
    c.execute('CREATE TABLE IF NOT EXISTS personaltasktable(task TEXT, reason TEXT, impact TEXT, task_status TEXT, task_start_date DATE, task_due_date DATE)')
    
def add_task_family(task, reason, impact, task_status, task_start_date, task_due_date):
    c.execute('INSERT INTO familytasktable(task, reason, impact, task_status, task_start_date, task_due_date) VALUES (?,?, ?, ?, ?, ?)', (task, reason, impact, task_status, task_start_date, task_due_date))
    conn.commit()

def view_all_data_family():
    c.execute('SELECT * FROM familytasktable')
    data = c.fetchall()
    return data

# Creating a table for family images
def fam_pics():
    c.execute('CREATE TABLE IF NOT EXISTS familyimages(id string, img blob)')
    
def add_family_pics(id, img):
    c.execute('INSERT INTO familyimages(id, img) VALUES (?, ?)', (id, sqlite3.Binary(img)))
    conn.commit()
    
def view_all_family_pics():
    c.execute('SELECT * FROM familyimages')
    data = c.fetchall()
    return data
    
    
# creating the tables for the Health 
def create_table_health():
    c.execute('CREATE TABLE IF NOT EXISTS personaltasktable(task TEXT, reason TEXT, impact TEXT, task_status TEXT, task_start_date DATE, task_due_date DATE)')
    
def add_task_health(task, reason, impact, task_status, task_start_date, task_due_date):
    c.execute('INSERT INTO healthtasktable(task, reason, impact, task_status, task_start_date, task_due_date) VALUES (?,?, ?, ?, ?, ?)', (task, reason, impact, task_status, task_start_date, task_due_date))
    conn.commit()
    
def view_all_data_health():
    c.execute('SELECT * FROM healthtasktable')
    data = c.fetchall()
    return data
    
# creating the tables for the Relationship 
def create_table_relationship():
    c.execute('CREATE TABLE IF NOT EXISTS personaltasktable(task TEXT, reason TEXT, impact TEXT, task_status TEXT, task_start_date DATE, task_due_date DATE)')
    
def add_task_relationship(task, reason, impact, task_status, task_start_date, task_due_date):
    c.execute('INSERT INTO relationshiptasktable(task, reason, impact, task_status, task_start_date, task_due_date) VALUES (?,?, ?, ?, ?, ?)', (task, reason, impact, task_status, task_start_date, task_due_date))
    conn.commit()
    
def view_all_data_relationship():
    c.execute('SELECT * FROM relationshiptasktable')
    data = c.fetchall()
    return data
    
    
# creating the tables for the Business 
def create_table_spiritual():
    c.execute('CREATE TABLE IF NOT EXISTS personaltasktable(task TEXT, reason TEXT, impact TEXT, task_status TEXT, task_start_date DATE, task_due_date DATE)')
    
def add_task_spiritual(task, reason, impact, task_status, task_start_date, task_due_date):
    c.execute('INSERT INTO spiritualtasktable(task, reason, impact, task_status, task_start_date, task_due_date) VALUES (?,?, ?, ?, ?, ?)', (task, reason, impact, task_status, task_start_date, task_due_date))
    conn.commit()
    
def view_all_data_spiritual():
    c.execute('SELECT * FROM spiritualtasktable')
    data = c.fetchall()
    return data