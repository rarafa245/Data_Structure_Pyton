from LinkedList import LinkedList

if __name__ == "__main__":
    minha_lista = LinkedList()
    minha_lista.append(7)
    minha_lista.append(8)
    minha_lista.append(9)
    minha_lista.append(10)
    print("Tamanho: {}".format(len(minha_lista)))
    print("Elemento {} : {}".format(1,minha_lista[1]))
    print("Index do elemento {} : {}".format(9,minha_lista.index(9)))
    minha_lista.insert(0,777)

    for i in range(len(minha_lista)):
        print(minha_lista[i])

    minha_lista.remove(10)
    print()

    for i in range(len(minha_lista)):
        print(minha_lista[i])

    print(minha_lista)
