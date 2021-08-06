#Função com While e break
def pedido():
    itens = []
    while True:
        ped = input("Informe um pedido:")
        if ped == "somente isso":
            break
        itens.append(ped)
    print("Esse é o seu pedido:\n", itens)

pedido()
