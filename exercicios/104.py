#!/usr/bin/python3

###
# Exercicios
###

# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]


def compa(a, b):
    if (a == b):
        return True
    else:
        return False

print(compa(list1, list2))


#
# 2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao necessarias.  Retorne True ou False.
def palind(a):
    if (a.lower().replace(' ', '') == a.lower().replace(' ', '')[::-1]):
        return True
    else:
        return False


print(palind("ovo"))
