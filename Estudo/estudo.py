def inverter_lista(lista):
    tamanho = len(lista)
    limite = tamanho//2
    for i in range(limite):
        aux = lista[i]
        lista[i] = lista[tamanho-1]
        lista[tamanho] = aux


lista = ["A","B","C","D","E","F","A"]

#inverter_lista(lista)
#print(lista)

def inverter_lista2(lista):
    nova_lista = []
    tamanho = len(lista)
    for i in range(tamanho):
        nova_lista.append(lista[tamanho-i-1])
    return nova_lista

#inverter_lista2(lista)
#print(lista)

def tem_duplicados(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False


tem_duplicados(lista)
#inverter_lista(lista)
print(lista)