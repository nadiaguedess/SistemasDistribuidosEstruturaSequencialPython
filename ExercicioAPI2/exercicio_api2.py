import requests
import sqlite3
import os
from datetime import datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))

chave_url = '9b96063b'

req = requests.get(f'https://api.hgbrasil.com/finance?key={chave_url}')
con = sqlite3.connect('bdcotacoes.db')

if req.status_code == 200:
    dict_main = req.json()
    
    valor_dolar = float(dict_main['results']['currencies']['USD']['buy'])
    valor_euro =  float(dict_main['results']['currencies']['EUR']['buy'])
    data_hora = datetime.now()
    
    query = "INSERT INTO moedas VALUES (?, ?, ?)"
    cursor = con.cursor()
    
    try:
        cursor.execute(query, (data_hora, valor_dolar, valor_euro))
        con.commit()
        print('Inserido com sucesso!')
    
    except Exception as e:
        con.rollback()
        print(f'Exception: {e}')
    
con.close()
