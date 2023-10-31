#
# autor: Michel
# data: 30/10/2023

# 2.	Em linguagem Python, faça um programa que leia 
# um grupo de valores
# e os armazene em uma lista, 
# imprima a lista e mostre o maior 
# elemento e a posição que ele se encontra.

# criando a lista vazia
lista1 = []
valor = 1 # valor diferente de 0 para entrar no while

while (valor != 0):
  valor = int(input("Digite um número (0->Sair): "))
  if valor != 0:
    lista1.append(valor)
    
# descobrir o maior elemento da lista
maior = max(lista1)

# descobrindo a posição do maior elemento
posicao = lista1.index(maior)
# ou 
for i in range(len(lista1)):
    if lista1[i] == maior:
        posicao = i
        
print(f"O maior elemento é {maior} e está na posição {posicao}")