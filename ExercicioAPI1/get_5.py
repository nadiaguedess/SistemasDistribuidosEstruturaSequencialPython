import requests
r = requests.get('http://www.google.com/search', params={'q': 'Centro Universitario UNA Aimores'})
if (r.status_code == 200):
    arq = open(r'c:\temp\retorno.html', 'w')
    arq.write(r.text)
    arq.close()
    print('\narquivo salvo')
else:
    print('Erro na requisicao.')