#
# autor: Michel
# data: 30/10/2023


# 3.	Em linguagem Python, faça um programa que crie uma agenda de
# telefones (3 contatos) que seja um dicionário para armazenar o 
# nome (chave) e armazene os números de telefones (elemento), cada 
# pessoa pode ter 1 ou mais números de telefones, fazendo a leitura 
# dos valores por meio de uma estrutura de repetição. Depois, crie 
# uma estrutura de repetição para listar todos os contados da agenda.

# criando a agenda (dicionário)
agenda = dict()

# lendo os contatos (nome e telefones)
for i in range(3):
  nome = input(f"Digite o nome do contato[{i+1}]: ")
  fones = list()
  while True:
    fone = input("Digite o telefone (0->Sair): ")
    if fone == "0":
      break
    fones.append(fone) # adicionando o telefone na lista de telefones
  agenda[nome] = fones # adicionando a lista de telefones no dicionário agenda

# listando a agenda
for nome in agenda:
  print(f"{nome} -> {agenda[nome]}")
  
# imprimir a agenda em dic
print(agenda) 
