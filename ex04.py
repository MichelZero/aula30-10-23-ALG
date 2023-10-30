#
# autor: Michel
# data: 30/10/2023

# 4.	Em linguagem Python, escreva um programa que leia os tempos 
# de 4 voltas (elemento) na pista em 3 competições (chave) de 
# um piloto de F-1, em seguida apresente a média dos tempos das 
# voltas nas 3 competições, e depois apresente qual a volta mais
# rápida em cada competição.

f1 = dict()
for i in range(3):
  pista = input(f"Digite o nome da pista[{i+1}]: ")
  voltas = list()
  while True:
    tempo = float(input("Digite o tempo (0->Sair): "))
    if tempo == 0:
      break
    voltas.append(tempo)
  f1[pista] = voltas
    
# apresentando a volta mais rápida em cada pista e a média dos tempos
for pista in f1.keys():
  print(f"{pista} -> {f1[pista]}")
  print(f"Volta mais rápida: {min(f1[pista])}")
  print(f"Média dos tempos: {sum(f1[pista])/len(f1[pista])}")
  print()