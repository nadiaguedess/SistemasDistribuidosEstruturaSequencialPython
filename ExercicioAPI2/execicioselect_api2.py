import sqlite3
from datetime import datetime

con = sqlite3.connect('bdcotacoes.db')

cur = con.cursor()
cur.execute("SELECT * FROM moedas")

rows = cur.fetchall()

for row in rows:
    print(row)
    
