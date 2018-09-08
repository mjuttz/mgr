import sqlite3
import hashlib
import RPi.GPIO as GPIO
from time import sleep

def match(barcode):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    t = hashlib.sha224(barcode.encode('utf-8')).hexdigest()
    
    c.execute('SELECT hash FROM DepositLockers WHERE hash = ?', (t,))
    query = c.fetchone()

    if query == ('5c24c24995926eb35f1db6d373442a5ea3e29b31999efe39928bca03',):
        print('succes')
        GPIO.output(21, GPIO.HIGH)
        sleep(3)
        GPIO.output(21, GPIO.LOW)
    elif query == ('513f50d9e1736929a9be1d8b31d009e139f8012855d76f336e88e71a',):
        print('succes')
        GPIO.output(16, GPIO.HIGH)
        sleep(3)
        GPIO.output(16, GPIO.LOW)
    else:
        print('fail')
