import requests
url = 'https://viacep.com.br/ws/'
list_ceps = ['32180140', '32180150', '32180160','32180170','32180180']
formato = '/xml/'
for cep in list_ceps:
    r = requests.get(url + cep + formato)
    if (r.status_code == 200):
        print()
        print(f'CEP : {cep}')
        print(f'XML : {r.text}')
        print()
    else:
        print('Erro na requisicao.')
