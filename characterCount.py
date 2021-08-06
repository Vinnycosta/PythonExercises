
#Contando caracteres sem contar espaços em branco
estados = ["São Paulo","Rio de Janeiro","Minas Gerais", "Rio Grande do Sul",
"Santa Catarina","Paraná"]

def contadorletra(list1):
    for index in list1:
        letras = len(index) - index.count(" ")
        print(f"{index} tem {letras} letras ")


contadorletra(estados)
