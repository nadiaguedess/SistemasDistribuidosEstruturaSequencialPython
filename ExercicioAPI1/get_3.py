import requests
rua = 'Rua Aimores'
prefix = 'https://viacep.com.br/ws/MG/Belo Horizonte/'
url = prefix + rua
formato = '/json/'
r = requests.get(url + formato)
if (r.status_code == 200):
    print()
    list_result = r.json()
    count = 0
    for result in list_result:
        count += 1
        print(f'Resultado {count}')
        for k in result:
            print(f'{k}: {result[k]}')
        print('\n')
else:
    print('Erro na requisicao.')
