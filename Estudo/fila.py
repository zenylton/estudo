def busca(lista, elem):
    """Retorna o Indice elem se ele estiver na lista ou None, caso contrário"""
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None

lista_estranha = [8, "S" , 32, 0, "Python", 11]
elemento = "nu"

indice = busca(lista_estranha, elemento)
if indice is not None:
    print(f"O indice do elemento {elemento} é {indice}")
else:
    print("O elemento {} não se encontra na lista".format(elemento))