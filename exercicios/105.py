#!/usr/bin/python3
###
# Exercicios
###

## Usando a lista: ['a','b','c']
# 1) Faca um loop para retornar: ['A','B','C']

list1 = ['a', 'b', 'c']
for x in range(len(list1)):
    print(list1[x].upper())

# OU

list1 = ['a', 'b', 'c']
for x in range(len(list1)):
    list1[x] = list1[x].upper()

print(list1)

## Usando os numeros: [0, 1, 3, 4, 5]
# 2) Faca um loop para retornar a soma de todos os elementos da listas
list2 = [0, 1, 3, 4, 5]
soma = 0
for x in range(len(list2)):
    soma = soma + list2[x]

print(soma)

# 3) Faca um loop para retornar apenas os numeros impares

list2 = [0, 1, 3, 4, 5]
impares = []
for x in range(len(list2)):
    if list2[x] % 2 != 0:
        impares.append(list2[x])

print(impares)

# OU

list2 = [0, 1, 3, 4, 5]
for x in range(len(list2)):
    if list2[x] % 2 != 0:
        print(list2[x])

## usando a string:~//
# 4) Conte quantas palavras de tamanho >= 5 existe nessa string
texto = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

aux = texto.split(' ')
contador = 0
for x in range(len(aux)):
    if len(aux[x]) >= 5:
        contador += 1
print(contador)

# 5) Usando list comprehension, crie uma lista com os multiplos de 3 de 0 ate 100
multiplos = [x * 3 for x in range(99) if (x * 3) <= 100]
print(multiplos)


# Faca uma funcao para encontrar os numeros primos no intervalo [2, 10), mas nao utilize a clausula else do for

print("---------------------------------------------")

for n in range(2, 10):
    auxiliar = 0
    for x in range(1, n+1):
        if n % x == 0:
            auxiliar += 1
    if auxiliar == 2:
        print("o numero {} é primo".format(n))