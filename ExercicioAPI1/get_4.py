import requests
url = 'https://viacep.com.br/UNA/'
cep = '30140071'
formato = '/json/'
r = requests.get(url + cep + formato)
if (r.status_code == 200):
    print()
    print(f'JSON : {r.json()}')
    print()
else:
    print(r.status_code)
    print('Erro na requisicao.')
    print(r.text)