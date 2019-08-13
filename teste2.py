# lista = ['a','b','c','d']
#
# for i in range(0, len(lista)-1):
#     print(lista[i])

# for i in range(0,10,2):
#     print(i)

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#
#     def obterNome(self):
#         return self.nome
#
#     def obterIdade(self):
#         return self.idade
#
#     def setIdade(self, idade):
#         self.idade = idade
#
# # p = Pessoa('marcos', 28)
# # print('Nome: %s' % p.obterNome())
# # print('Idade: %d' % p.obterIdade())
#
# p1 = Pessoa('Marcos',28)
# p2 = Pessoa('João',20)
# p3 = Pessoa('Maria',18)
#
#
# pessoas = []
#
# pessoas.append(p1)
# pessoas.append(p2)
# pessoas.append(p3)
#
# for pessoa in pessoas:
#     print(pessoa.obterIdade())
#
# Pessoa.setIdade(p1,12)
# print(p1.obterIdade())

#Lista de numeros pares

pares = [num for num in range(101) if (num % 2 == 0)]
print(pares)