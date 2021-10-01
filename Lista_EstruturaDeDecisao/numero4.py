letra = input("Digite a letra:")
vogais = ['a', 'e', 'i', 'o', 'u']

if(letra.lower() in vogais):
    print("É uma vogal")
else:
    print("É uma consoante")