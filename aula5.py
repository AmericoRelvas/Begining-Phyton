# -*- coding: utf-8 -*-
"""aula5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_GBccV1mS-UPjUK8pYSzSwd6ksvMAQGC
"""

nomes = 'João Marcela Sonia Daryl Vernon Eder Mechelle Edan Igor Ethan Reed Travis Hoyt'.split()
print('Marcela' in nomes)
print('Roberto' in nomes)

def executar_busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
    return False

import random
lista = random.sample(range(1000), 50)
print(sorted(lista))
executar_busca_linear(lista, 10)

vogais = 'aeiou'
resultado = vogais.index('e')
print(resultado)

def procurar_valor(lista, valor):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        if valor == lista[i]:
            return i
    return None

vogais = 'aeiou'
resultado = procurar_valor(lista=vogais, valor='a')
if resultado != None:
    print(f"Valor encontrado na posição {resultado}")
else:
    print("Valor não encontrado")

def procurar_valor(lista, valor):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        if valor == lista[i]:
            return i
    return None   
def testar_resultado(resultado):
  if resultado:
      print(f"Valor encontrado an posição {resultado}")
  else:
      print("Valor não encontrado")  
vogais = ['a', 'e', 'i', 'o', 'u']
# Usando nossa função
resultado = procurar_valor(lista=vogais, valor='o')
testar_resultado(resultado)
# Usando a função index - descomente as linhas a seguir para testar
#resultado = vogais.index('z')
#testar_resultado(resultado)

def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:
        # Encontra o elemento que divide a lista ao meio
        meio = (minimo + maximo) // 2
        # Verifica se o valor procurado está a esquerda ou direita do valor central
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True # Se o valor for encontrado para aqui
    return False # Se chegar até aqui, significa que o valor não foi encontrado

lista = list(range(1, 50))

print(lista)

print('\n',executar_busca_binaria(lista=lista, valor=10))
print('\n', executar_busca_binaria(lista=lista, valor=200))

def procurar_valor(lista, valor):
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:
        meio = (minimo + maximo) // 2
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return meio 
    return None

vogais = ['a', 'e', 'i', 'o', 'u']
resultado = procurar_valor(lista=vogais, valor='o')
if resultado:
    print(f"Valor encontrado na posição {resultado}")
else:
    print("Valor não encontrado")

# Parte 1 - Implementar o algoritmo de busca linear
def executar_busca_linear(lista, valor):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        if valor == lista[i]:
            return True
    return False

# Parte 2 - Criar a função que faz o dedup e os tratamentos no cpf
def criar_lista_dedup(lista):
    lista_dedup = []
    for cpf in lista:
        cpf = str(cpf)
        cpf = cpf.replace("-", "").replace(".", "")
        if len(cpf) == 11:
            if not executar_busca_linear(lista_dedup, cpf):
                lista_dedup.append(cpf)

    return lista_dedup

# Parte 3 - Criar uma função de teste
def testar_funcao(lista_cpfs):
    lista_dedup = criar_lista_dedup(lista_cpfs)
    print(lista_dedup)

    
lista_cpfs = ['111.111.111-11', '11111111111', '222.222.222-22', '333.333.333-33', '22222222222', '444.44444']
testar_funcao(lista_cpfs)