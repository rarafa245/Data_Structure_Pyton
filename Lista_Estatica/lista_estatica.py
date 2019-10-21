#-*-coding:latin1 -*-
def buscar_lista(lista, element):
    if element in lista:
        return lista.index(element)
    else:
        return None

def acrescentar_Elemento(lista, elemento, posicao):
    if posicao == len(lista):
        lista.append(elemento)
        return lista
    elif posicao < len(lista):
        nova_Lista1 = lista[:posicao]
        nova_Lista1.append(elemento)
        nova_Lista1 = nova_Lista1 + lista[posicao:]
        return nova_Lista1
    else:
        return None

def remover_elemento_posicao(lista,posicao):
    if posicao == None:
        return None
    if posicao < len(lista):
        lista.pop(posicao)
        return lista
    else:
        return None

def remover_elemento_nome(lista,elemento):
    return remover_elemento_posicao(lista, buscar_lista(lista,elemento))


if __name__ == "__main__":
    lista = ["Ola", "Meu", "Nome", "é", "Rafael"]
    print(buscar_lista(lista, "Rafael"))
    lista = acrescentar_Elemento(lista, "não", 0)
    print(lista)
    lista = remover_elemento_posicao(lista,0)
    print(lista)
    lista = remover_elemento_nome(lista, "é")
    print(lista)