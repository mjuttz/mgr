import sqlite3
import hashlib

def match(barcode):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    t = hashlib.sha224(barcode.encode('utf-8')).hexdigest()
    
    c.execute('SELECT hash FROM uzytkownicy WHERE hash = ?', (t,))
    query = c.fetchone()

    if query:
        print('succes')
    else:
        print('fail')
