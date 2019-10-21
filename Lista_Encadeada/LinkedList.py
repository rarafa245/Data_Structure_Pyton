#-*-coding:latin1-*-
from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        """Acrescenta Elemento na Lista (Ligação de Objetos Instanciados)
            - Caso head aponte outros elementos : Percorrer a lista até achar ultimo nó
            - Caso head não aponte para outros elementos : Inserção direta em head
        """
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)
        self._size = self._size +1

    def _getnode(self, index):
        """Percorrendo a Lista e retorna o nó que está na posição 'index' """
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of Range")
        return pointer


    def __len__(self):
        """Retorna o Tamanho da Lista usando metodo len()"""
        return self._size

    def __setitem__(self, index, elem):
        # lista[5] = 9
        # lista.set(5) = 9

        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("List index out of Range")

    def __getitem__(self, index):
        # a = lista[6]
        # a = lista.get(6)

        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("List index out of Range")

    def index(self, elem):
        """Retorna o Indice do Elemento na Lista"""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError("{} is not in list".format(elem))

    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index - 1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1


    def remove(self, elem):
        if self.head == None:
            raise ValueError("No Elements in List")
        elif self.head.data == elem:
            self.head.data = self.head.next
        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer:
                if (pointer.data == elem):
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size -= 1
                    return
                ancestor = pointer
                pointer = pointer.next
            raise ValueError("{} is not in List".format(elem))

    def __repr__(self):
        """Criando uma Representação: print(lista)"""
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()
