#!/usr/bin/python3

weekdays = ['mon','tues','wed','thurs','fri']
days_list = ['mon','tues','wed','thurs','fri','sat','sun']
list = ['a', 1, 3.14159265359]
# ex 102 #

# Como selecionar 'wed' pelo indice?
print(weekdays.__getitem__(2))

# Como verificar o tipo de 'mon'?

tipo = weekdays.__getitem__(0)
print( type(tipo))

# Como separar 'wed' até 'fri'?

print(weekdays[2:5])

# Quais as maneiras de selecionar 'fri' por indice?


print(weekdays[4])

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