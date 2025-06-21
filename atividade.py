'''
def quantidade_digito(valor):
    return len(str(valor))

numero = int(input('Digite o valor: '))
print(quantidade_digito(numero))
'''

frase = input('Digite algo: ')

def comeco_maiusculo(frase):
    return frase.capitalize()

print(comeco_maiusculo(frase))

def tudo_maisculo(frase):
    return frase.upper()

print(tudo_maisculo(frase))

def troce_letras(frase):
    return frase.replace('a', 'e')

print(troce_letras(frase))

def conta(frase):
    return frase.count('a')

print('Na frase tem:', conta(frase),'a')

def quantidade_digito(frase):
    return len(str(frase))

print(quantidade_digito(frase), 'caracteres')