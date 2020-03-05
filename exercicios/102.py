#!/usr/bin/python3

weekdays = ['mon','tues','wed','thurs','fri']
days_list = ['mon','tues','wed','thurs','fri','sat','sun']
list = ['a', 1, 3.14159265359]
# exercicio 102 #

# Como selecionar 'wed' pelo indice?
print(weekdays.__getitem__(2))
teste = weekdays[2]
print(teste)
# Como verificar o tipo de 'mon'?
teste = weekdays[0]
print(type(teste))

# Como separar 'wed' até 'fri'?

print(weekdays[2:5])

days = weekdays[2:]
print(days)

# Quais as maneiras de selecionar 'fri' por indice?
teste1 = weekdays[4]
teste2 = weekdays[4:]
teste3 = weekdays[-1]
print(teste1)
print(teste2)
print(teste3)

# Qual eh o tamanho dos dias e days_list?

print(len(days))
print(len(days_list))

# Como inverter a ordem dos dias?

days.reverse()
days[::-1]

# Como inserir a palavra 'zero' entre 'a' e 1 de list?

list.insert(1,"zero")

# Como limpar list?

list.clear()

# Como deletar list?

del(list)

# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?

ultimo_elemento = list[len(list)-1]
list.remove(ultimo_elemento)
