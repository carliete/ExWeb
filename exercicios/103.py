###
# Exercicios
###

# 1) Extraia o titulo do livro da string
# 2) Salve o titulo de cada livro em uma variável

book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'
aux1 = book1.split('by')
aux2 = book2.split('by')
aux3 = book3.split('by Nassim')

titulo1 = aux1[0]
titulo2 = aux2[0]
titulo3 = aux3[0]

# 3) Quantos caracteres cada título tem?
print(len(titulo1))
print(len(titulo2))
print(len(titulo3))

# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}
at1 = aux1[1]
at2 = aux2[1]
at3 = " Nassim" + aux3[1]

auxat = at1.split(",")
auxat2 = at2.split(",")
auxat3 = at3.split(",")

autor1 = auxat[0]
autor2 = auxat2[0]
autor3 = auxat3[0]
ano1 = auxat[1]
ano2 = auxat2[1]
ano3 = auxat3[1]

print("{0}-{1},{2}".format(titulo1, autor1, ano1))
print("{0}-{1},{2}".format(titulo2, autor2, ano2))
print("{0}-{1},{2}".format(titulo3, autor3, ano3))




# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta
palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'

if palindrome_one.lower().replace(' ','') == palindrome_one.lower().replace(' ','')[::-1]:
  print(palindrome_one.lower() + " é palindrome perfeita")
else:
  print(palindrome_one.lower() + " não é palindrome perfeita")

if palindrome_two.lower().replace(' ','') == palindrome_two.lower().replace(' ','')[::-1]:
  print(palindrome_two.lower() + " é palindrome perfeita")
else:
  print(palindrome_two.lower() + " não é palindrome perfeita")

if palindrome_three.lower().replace(' ','') == palindrome_three.lower().replace(' ','')[::-1]:
  print(palindrome_three.lower() + " é palindrome perfeita")
else:
  print(palindrome_three.lower() + " não é palindrome perfeita")

if palindrome_four.lower().replace(' ','') == palindrome_four.lower().replace(' ','')[::-1]:
  print(palindrome_four.lower() + " é palindrome perfeita")
else:
  print(palindrome_four.lower() + " não é palindrome perfeita")

