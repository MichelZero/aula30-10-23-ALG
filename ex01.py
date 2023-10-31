#
# autor: Michel
# data: 30/10/2023
#
# 1.	Em linguagem Python, faça um programa que leia um grupo de
#  números inteiros, armazenando-o em uma lista (L1), calcular 
# o quadrado dos elementos dessa lista, armazenando o resultado em 
# oura lista (L2), imprimir todas as listas.


# criando a lista vazia 
lista1 = []
valor = 1 # valor diferente de 0 para entrar no while

while (valor != 0):
  valor = int(input("Digite um número (0->Sair): "))
  if valor != 0:
    lista1.append(valor)

# descobrir o tamanho da lista1 
# criar uma lista2 com o mesmo tamanho da lista1
lista2 = list(range(len(lista1)))

for i in range(len(lista1)):
    lista2[i] = lista1[i] * lista1[i] # lista2[i] = lista1[i]**2
    

# imprimir as listas
# lista 1
print(f"Lista 1: {lista1}")

# lista 2
print("Lista 2: ", end="")
for i in range(len(lista2)):
    print(lista2[i], end=" ")