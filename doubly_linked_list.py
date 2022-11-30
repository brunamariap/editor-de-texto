class Node:

    def __init__(self, data, prev_node, next_node):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node


class DoublyLinkedList:
    def __init__(self):
        #são 2 referencias que nao podem sair
        self.header = Node(None, None, None)
        self.tail = Node(None, None, None)
        
        self.header.next_node = self.tail
        self.tail.prev_node = self.header
        
        self.size = 0

    def is_empty(self):
        """ Checa se a lista está vazia """
        return self.size == 0

    def __len__(self):
        return self.size

    def print_list(self):
        cur_node = self.header.next_node
        """ print('\nElementos da lista:', end=' ') """
        while cur_node.next_node != None:
            print(cur_node.data, end='')
            cur_node = cur_node.next_node
    
    def insert_between(self, item, predecessor, sucessor):
        new_node = Node(item, predecessor, sucessor)
        #muda os ponteiros
        predecessor.next_node = new_node
        sucessor.prev_node = new_node
        self.size += 1

    def insert_first(self, data):
        # Nó deve entrar entre headerer e headerer.next
        self.insert_between(data, self.header, self.header.next_node)

    def insert_last(self, data):
        self.insert_between(data, self.tail.prev_node, self.tail)

    def delete_node(self, node): #passar nó que quero apagar
        # Referência para o antecessor e o sucessor do nó que quero apagar
        predecessor = node.prev_node 
        sucessor = node.next_node

        # Remove o nó pois os ponteiros para ele não existem mais
        predecessor.next_node = sucessor
        sucessor.prev_node = predecessor

        """ self.current_node = predecessor.next_node """

        self.size -= 1

    def delete_last(self):
        if self.is_empty():
            print('Lista vazia!')
        return self.delete_node(self.tail.prev_node) #passo o último nó para ser deletado

    def delete_first(self):
        if self.is_empty():
            print('Lista vazia!')
        return self.delete_node(self.header.next_node) #passo o primeiro nó para ser deletado

    def search(self, data):
        cur_node = self.header
        while cur_node.data != data:
            print(f'\nO dado: {data} foi encontrado')
            return 
        cur_node = cur_node.next_node

    def clear(self):
        self.header.next_node = None
        self.tail.prev_node = None
        
        self.header.next_node = self.tail
        self.tail.prev_node = self.header
        
        self.size = 0
    
    def mover(self, tecla):
        key_press = tecla
        if key_press == 'right':
            if self.current_node.next_node is None: # Chegou no final
                self.current_node = self.tail.prev_node 
            else:
                self.current_node = self.current_node.next_node
        elif key_press == 'left':
            if self.current_node.prev_node is None: # Chegou no início
                self.current_node = self.header.next_node
            else:
                self.current_node = self.current_node.prev_node

    def insert(self, dado):
        """ função que deve chamar insert_between para inserir um número em qualquer lugar """
        if self.is_empty():
            self.current_node = self.tail.prev_node

        self.insert_between(dado, self.current_node, self.current_node.next_node)
        self.current_node = self.current_node.next_node

    def delete(self):
        """ Função que deve deletar qualquer coisa chamando a função delete_node"""
        self.delete_node(self.current_node)