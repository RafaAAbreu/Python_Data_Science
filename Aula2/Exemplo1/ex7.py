'''
Comentario de mais de uma linha
'''

nome , idade,cidade = input(
    "Digite o nome, idade e cidade separado por espaço: "
).split()

idade = int(idade)

print(f"{nome} tem {idade} anos e mora em {cidade}")