dicionario = {'marcos':28, 'joao':27, 'maria':19}

#print(len(d))

# for indice in dicionario:
#     print(dicionario[indice])

# num = 11
#
# if(num % 2 == 0):
#     print("Par")
# else:
#     print("Impar")

#criação de função usar o "def"

def par(num):
    if (num % 2 == 0):
        return True
    return False

print(par(11))